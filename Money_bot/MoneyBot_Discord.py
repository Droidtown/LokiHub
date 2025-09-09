#!/user/bin/env python
# -*- coding: utf-8 -*-

import discord
import json
import logging
import os
import re


from ArticutAPI import Articut
from discord import app_commands
from discord.ext import commands
from pprint import pprint
from requests import post
from Money_add.main  import askLoki, askLLM

help_text = """
**Money 記帳小幫手 使用指南**

📌 基本指令
------------------------------
**/add <文字>**
➤ 新增一筆記帳紀錄  
   範例：`/add 昨天花了150元搭計程車`  
   ✅ 自動抓取：日期、收支類別、事項、數量、金額

**/view**
➤ 查看所有紀錄  
   範例：`/view`  
   ✅ 顯示完整收支明細與統計 (總收入、總支出、收支差額)

**/view <文字>**
➤ 搜尋特定紀錄  
   範例：`/view 8月的飲食支出`  
   ✅ 可輸入日期 / 收支 / 類別，進行過濾

**/report <文字>**
➤ 回報錯誤或無法識別的句子  
   範例：`/report 花了一百塊錢請客`  
   ✅ 協助改進系統

**/help**
➤ 顯示這份說明

⚠️ 注意事項
------------------------------
1. 每位使用者有自己的紀錄檔，不會互相干擾。  
2. 請輸入至少「金額 + 事項」，否則無法新增。  
3. 每次僅能處理一則紀錄。
4. 金額自動判斷收入 / 支出，支出會顯示為負數。  

❌ 常見錯誤示例
------------------------------
- `/add 買蛋糕`  
   → ⚠️ 缺少金額，無法新增  

- `/add 花了200元`  
   → ⚠️ 缺少事項，無法新增  

- `/view` + 沒有輸入條件  
   → ✅ 顯示所有紀錄  

- `/view 薪水`  
   → ✅ 僅顯示「薪資」相關紀錄
"""

purgedPAT = re.compile("</?[A-Za-z]+(_[A-Za-z]+)?>")
spacePAT = re.compile("(?<=\d)\s+(?=\d)")
yearPAT = re.compile("<ENTITY_num>(2\w{3})</ENTITY_num>")
datePAT =  [
    re.compile("<ENTITY_num>(0?[1-9]|1[0-2])</ENTITY_num><UserDefined>/</UserDefined><ENTITY_num>(0?[1-9]|[12][0-9]|3[0-1])</ENTITY_num>"),
    re.compile("<TIME_month>([^<]+)月</TIME_month><ENTITY_num>([^<]+)</ENTITY_num>")
]
moneyPAT = [
    re.compile("<ENTITY_num>([^<]+)</ENTITY_num>"), 
    re.compile("<ENTITY_classifier>([^<]+)塊</ENTITY_classifier>(?!<(?:MODIFIER|ModifierP)>[^<]+</(?:MODIFIER|ModifierP)>)(?!<DegreeP>[^<]+</DegreeP>)(?!<(?:UserDefined|ENTITY_(?:noun(?:Head|y)?|oov))>[^<]+</(?:UserDefined|ENTITY_(?:noun(?:Head|y)?|oov))>)")
]

def getDateTime(uttSTR, timeRef=None):
    """
    求出時間(2025-08-28)
    """
    if timeRef:
        resultDICT = articut.parse(uttSTR, level="lv3", timeRef=timeRef, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
    else:
        resultDICT = articut.parse(uttSTR, level="lv3", userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
    return resultDICT["time"]
def getNumber(uttSTR):
    '''
    求出數值
    '''
    resultDICT = articut.parse(uttSTR, level="lv3", userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
    return resultDICT["number"]
def insertUtterance(username, lokiKey, projectNameSTR, intentNameSTR, utteranceLIST):
    '''
    將輸入存進intent
    '''
    url = "https://api.droidtown.co/Loki/Call/"
    payload = {
            "username" : username,
            "loki_key" : lokiKey,
            "project": projectNameSTR, 
            "intent": intentNameSTR,
            "func": "insert_utterance",
            "data": {
                "utterance": utteranceLIST
            }
        }
    response = post(url, json=payload)
    response = response.json()
    pprint(response)
    return response

def add_preprocessing(uttSTR): 
    try:
        '''
        前處理1：去掉標點符號，存為uttSTR
        '''        
        articutResult1 = articut.parse(uttSTR, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
        uttSTR = ""
        for i in articutResult1["result_pos"]:
            if len(i) <= 1:
                pass
            else:
                uttSTR += purgedPAT.sub("", i)
        '''
        前處理2：將uttSTR中的日期、金額正規化(X月Y日、X元)
        '''
        uttSTR = spacePAT.sub('$$$', uttSTR).replace("-", "/")
        articutResult2 = articut.parse(uttSTR, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")        
        for pat in datePAT:
            match = pat.findall(articutResult2["result_pos"][0])
            if match:
                articutResult2["result_pos"][0] = pat.sub(f"{match[0][0]}月{match[0][1]}日", articutResult2["result_pos"][0], count = 1)
        for pat in moneyPAT:
            match = pat.findall(articutResult2["result_pos"][0])
            if match:
                articutResult2["result_pos"][0] = pat.sub(f"{match[0]}元", articutResult2["result_pos"][0], count = 1)
        uttSTR =  purgedPAT.sub("", articutResult2["result_pos"][0]).replace("$$$", " ")
        return uttSTR
    except Exception as e:
        logging.error(f"add_preprocessing錯誤: {e}")
        raise RuntimeError("⚠️ 新增紀錄失敗，請檢查輸入格式或換句話說～")

    
def add_postprocessing(resultDICT, uttSTR, category):
    try:
        
        '''
        後處理1：去除<...></...>
        '''
        for i in resultDICT:
            if resultDICT[i]:
                resultDICT[i][0] =  purgedPAT.sub("", resultDICT[i][0])
        '''
        後處理2：透過getDateTime抓出"date"(2025-08-21)
        '''
        if resultDICT["time"]:
            resultDICT["date"] = [getDateTime(uttSTR)[-1][0]["datetime"].split()[0]]
        else:
            resultDICT["date"] = [getDateTime("今天")[-1][0]["datetime"].split()[0]]
        '''
        後處理3：若是沒有明確的量詞就設為1
        '''
        if resultDICT["amount"] == []:
            resultDICT["amount"] = ['1']
        '''
        後處理4：將amount, money中的中文數字轉成阿拉伯數字
        '''
        resultDICT["amount"][0] = list(getNumber(resultDICT["amount"][0]).values())[0]
        resultDICT["money"][0] = list(getNumber(resultDICT["money"][0]).values())[0]
        
        '''
        後處理5：由LLM判斷是支出或收入並找出category，若為支出金額為負數
        '''
        resultDICT["type"] = [category.classify(uttSTR)["type"]]
        resultDICT["category"] = [category.classify(uttSTR)["category"]]
        if resultDICT["type"][0] == "支出":
            resultDICT["money"][0] = -resultDICT["money"][0]    
        '''
        後處理6：篩出要儲存的部分
        '''
        allowed_keys = {"date", "content", "amount", "money", "type", "category", "text"}
        resultDICT = {k: resultDICT[k] for k in allowed_keys if k in resultDICT} 
        return resultDICT
    except Exception as e:
        logging.error(f"add_postprocessing錯誤: {e}")
        raise RuntimeError("⚠️ 新增紀錄失敗，請檢查輸入格式或換句話說～")
   

def view_preprocessing(uttSTR, category):
    
    try:
        '''
        前處理1：去掉標點符號，存為uttSTR
        '''        
        articutResult1 = articut.parse(uttSTR, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
        uttSTR = ""
        for i in articutResult1["result_pos"]:
            if len(i) <= 1:
                pass
            else:
                uttSTR += purgedPAT.sub("", i)
        '''
        前處理2：將uttSTR中的年份、日期正規化(X月Y日、X年)
        '''
        uttSTR = spacePAT.sub('$$$', uttSTR).replace("-", "/").replace("份", "")
        articutResult2 = articut.parse(uttSTR, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
        match = yearPAT.findall(articutResult2["result_pos"][0])
        if match:
            articutResult2["result_pos"][0] = yearPAT.sub(f"{match[0]}年", articutResult2["result_pos"][0], count = 1)
        for pat in datePAT:
            match = pat.findall(articutResult2["result_pos"][0])
            if match:
                articutResult2["result_pos"][0] = pat.sub(f"{match[0][0]}月{match[0][1]}日", articutResult2["result_pos"][0], count = 1)
        uttSTR =  purgedPAT.sub("", articutResult2["result_pos"][0]).replace("$$$", " ")
        '''
        前處理3:找出欲搜尋之時間、收支類別
        '''
        articutResult3 = articut.parse(uttSTR, userDefinedDictFILE="./Money_add/intent/USER_DEFINED.json")
        result = category.classify(uttSTR)
        if "<TIME_day>" in articutResult3["result_pos"][0]:
            result["time"] = getDateTime(uttSTR)[-1][0]["datetime"].split()[0]
        elif "<TIME_month>" in articutResult3["result_pos"][0]:
            result["time"] =  getDateTime(uttSTR)[-1][0]["datetime"].split()[0][0:7]
        elif "<TIME_year>" in articutResult3["result_pos"][0]:
            result["time"] =  getDateTime(uttSTR)[-1][0]["datetime"].split()[0][0:4]
        else:
            result["time"] = None
        if result["type"] == "無法判斷":
            result["type"] = None
        if result["category"] == "無法判斷":
            result["category"] = None        
        return result

    except Exception as e:
        logging.error(f"view_preprocessing錯誤: {e}")
        raise RuntimeError("⚠️ 搜尋紀錄失敗，請檢查輸入格式或換句話說～")

    
class Record:
    def __init__(self, user_name, user_id):
        self.folder = f"./Data/{user_name}_{user_id}"
        os.makedirs(self.folder, exist_ok=True)
        self.RecordFile = os.path.join(self.folder, "RecordFile.json")
        self.load_RecordFile()

    def load_RecordFile(self):
        '''
        開啟記錄檔案，若沒有直接建一個
        '''    
        try:
            with open(self.RecordFile, "r", encoding="utf-8") as f:
                self._recordList = json.load(f)
        except:
            self._recordList = [
                f"{'日期':<11}{'收支':<6}{'類別':<10}{'事項':<14}{'數量':>6}{'金額':>12}",
                "-" * 80
            ]

    def save_RecordFile(self):
        '''
        存檔
        '''        
        with open(self.RecordFile, "w", encoding="utf-8") as f:
            json.dump(self._recordList, f, ensure_ascii=False, indent=2)
        print("紀錄已存檔")

    def add(self, text, category, user_name):
        """
        新增一則紀錄，並照時間重新排序。若缺少金額或事項則會停止
        """        
        try:
            refDICT = {"date": [], "type": [],"category": [],"content": [], "amount": [], "money": [], "time": [], "text": [text]} 
            add_preResult = add_preprocessing(text)
            add_lokiResult = askLoki(add_preResult, refDICT=refDICT)
            add_postResult = add_postprocessing(add_lokiResult, add_preResult, category)
            missing = []
            if add_postResult["content"] == []:
                missing.append("事項")
            if add_postResult["money"] == []:
                missing.append("金額")
            if missing:
                raise RuntimeError(f"⚠️ 新增紀錄失敗，缺少：{'、'.join(missing)}，請檢查輸入格式")
            record = (
                f'{add_postResult["date"][0]:<12}'
                f'{add_postResult["type"][0]:<6}'
                f'{add_postResult["category"][0]:<10}'
                f'{add_postResult["content"][0]:<14}'
                f'{add_postResult["amount"][0]:>6}'
                f'{add_postResult["money"][0]:>14,}\n'
                f'      原始輸入：{add_postResult["text"][0]}'
            )
            self._recordList.append(record)
            msg = []
            msg.append(f"{user_name}新增紀錄：\n")
            msg.append(self._recordList[0])
            msg.append(self._recordList[1])
            msg.append(self._recordList[-1])
            msg.append("-" * 80)
            self._recordList[2:] = sorted(self._recordList[2:], key=lambda r: r.split("\n")[0].split()[0])            
            print(f"{user_name}新增紀錄：「{text}」")
            self.save_RecordFile()
            return "\n".join(msg)

        except Exception as e:
            logging.error(f"新增紀錄錯誤: {e}")
            raise RuntimeError(str(e))

    def view(self, user_name):
        '''
        檢視完整紀錄
        '''        
        if len(self._recordList) <= 2:
            return "空空如也～快去記帳吧～"
        try:
            income = 0
            expense = 0
            msg = []
            msg.append(f"{user_name}的記帳紀錄：\n")
            for i, record in enumerate(self._recordList, start=1):
                if i == 1:
                    msg.append(f"{'':<4}{record}")
                    continue
                elif i == 2:
                    msg.append(record)
                    continue
                num = int(record.split("\n")[0].split()[-1].replace(",", ""))
                if num >= 0:
                    income += num
                else:
                    expense += num
                msg.append(f"{i - 2:<4}{record}")
            msg.append("-" * 80)
            msg.append(f"💰 總收入：{income:>12,} 元")
            msg.append(f"💸 總支出：{expense:>12,} 元")
            msg.append(f"📊 收支差額：{income + expense:>12,} 元")
            print(f"{user_name}檢視紀錄")
            return "\n".join(msg)
        except Exception as e:
            logging.error(f"檢視紀錄錯誤: {e}")
            raise RuntimeError("⚠️ 檢視紀錄失敗，請檢查輸入格式或換句話說～")


    
    def search(self, text, category, user_name):
        """
        按照輸入內容過濾紀錄 (日期、收支、類別)
        """
        try:
            view_preResult = view_preprocessing(text, category)
            #排除三個條件皆None的情形
            if not any([view_preResult["time"], view_preResult["type"], view_preResult["category"]]):
                return "⚠️ 請至少輸入日期、收支或類別來搜尋～"
    
            income = 0
            expense = 0
            msg = []
            msg.append(f"{user_name}的記帳紀錄：\n「{text}」")
            msg.append(f"「時間：{view_preResult['time']} / 收支：{view_preResult['type']} / 類別：{view_preResult['category']}」\n")
            
            found = False
            for i, record in enumerate(self._recordList, start=1):
                if i == 1:
                    msg.append(f"{'':<4}{record}")
                    continue
                elif i == 2:
                    msg.append(record)
                    continue
                
                record_date = record.split("\n")[0].split()[0]
                record_type = record.split("\n")[0].split()[1]
                record_category = record.split("\n")[0].split()[2]
                record_num = int(record.split("\n")[0].split()[-1].replace(",", ""))
        
                time_match = (view_preResult["time"] is None or view_preResult["time"] in record_date)
                type_match = (view_preResult["type"] is None or view_preResult["type"] == record_type)
                category_match = (view_preResult["category"] is None or view_preResult["category"] == record_category)
    
                #抓出同時滿足條件的紀錄
                if time_match and type_match and category_match:
                    found = True
                    msg.append(f"{i-2:<4}{record}")
                    if record_num >= 0:
                        income += record_num
                    else:
                        expense += record_num
            #找不到同時滿足條件的紀錄
            if not found:
                return f"找不到「{text}」的相關紀錄～\n「時間：{view_preResult['time']} / 收支：{view_preResult['type']} / 類別：{view_preResult['category']}」"
    
            msg.append("-" * 80)
            msg.append(f"💰 總收入：{income:>12,} 元")
            msg.append(f"💸 總支出：{expense:>12,} 元")
            msg.append(f"📊 收支差額：{income + expense:>12,} 元")
            print(f"{user_name}搜尋紀錄：「{text}」")
            return "\n".join(msg)
    
        except Exception as e:
            logging.error(f"搜尋紀錄錯誤: {e}")
            raise RuntimeError("⚠️ 搜尋紀錄失敗，請檢查輸入格式或換句話說～")

    def delete(self, index, user_name):
        '''
        刪除紀錄
        '''
        if len(self._recordList) <= 2:
            return "⚠️ 空空如也～沒有任何紀錄可以刪除～"
    
        try:

            real_index = index + 1
            if real_index >= len(self._recordList) or index < 1:
                return f"⚠️ 找不到編號 {index} 的紀錄"
    
            deleted_record = self._recordList.pop(real_index)
            self.save_RecordFile()
            msg = []
            msg.append(f"{user_name} 刪除了紀錄：\n")
            msg.append(self._recordList[0])
            msg.append(self._recordList[1])                            
            msg.append(deleted_record)
            msg.append("-" * 80)
            msg.append("\n\n(剩下的紀錄)")
            msg.append(self.view(user_name))
            print(f"{user_name}刪除了第 {index} 筆紀錄")
            insertUtterance(
                username=accountDICT["username"], 
                lokiKey=accountDICT["loki_key"], 
                projectNameSTR="Money_add", 
                intentNameSTR="check", 
                utteranceLIST=[deleted_record.split("\n")[1]]
            )
            return "\n".join(msg)
        except Exception as e:
            logging.error(f"刪除紀錄錯誤: {e}")
            raise RuntimeError("⚠️ 刪除紀錄失敗，請檢查輸入格式或換句話說～")        



class Category:
    def __init__(self, user_name, user_id):
        self.folder = f"./Data/{user_name}_{user_id}"
        os.makedirs(self.folder, exist_ok=True)
        self.CategoryFile = os.path.join(self.folder, "CategoryFile.json")
        self.load_CategoryFile()

    def load_CategoryFile(self):
        '''
        開啟類別檔案，若沒有直接建一個
        '''
        try:
            with open(self.CategoryFile, "r", encoding="utf-8") as f:
                self._categoryList = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # 此為預設類別，可自行更改
            # 若已存有 CategoryFile，則會以檔案內容為主，不會使用這份預設清單。
            self._categoryList = [
                "飲食",
                "交通",
                "日用品",
                "居家",
                "稅務",
                "娛樂",
                "旅遊",
                "醫療",
                "教育",
                "電子",
                "美妝",
                "運動",
                "其他",
                "薪資",
                "獎金",
                "投資", 
            ]
            self.save_categories()

    def save_categories(self):
        '''
        存檔
        '''
        with open(self.CategoryFile, "w", encoding="utf-8") as f:
            json.dump(self._categoryList, f, ensure_ascii=False, indent=2)

    def classify(self, uttSTR):
        '''
        由Gemma2-9B判斷收支、類別
        '''
        options = "、".join(self._categoryList)
        prompt = (
            f"請判斷「{uttSTR}」這句話屬於支出還是收入，並判斷是什麼類別 (從 {options} 中選擇)，"
            "若無法判斷請回答無法判斷\n"
            "回答格式：\n"
            "收支：XXX\n"
            "類別：YYY"
        )
        try:
            llmReply = askLLM(prompt).strip()
        except:
            llmReply = "收支：無法判斷\n類別：無法判斷"
        #回答內容預設為"無法判斷"
        classifyResult = {"type": "無法判斷", "category": "無法判斷"}
        if "支出" in llmReply:
            classifyResult["type"] = "支出"
        elif "收入" in llmReply:
            classifyResult["type"] = "收入"
    
        if "無法判斷" not in llmReply:
            for category in self._categoryList:
                if category in llmReply:
                    classifyResult["category"] = category
                    break
        return classifyResult


class Client(commands.Bot):
    async def on_ready(self):
        print('{}上線囉～({})'.format(self.user, self.user.id))
        
        try:
            guild = discord.Object(id=accountDICT["server_id"])
            synced = await self.tree.sync(guild = guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
       
        except Exception as e:
            print(f'Error syncing command: {e}')
    async def on_message(self, message):
        if message.author == self.user:
            return
        logging.debug("收到來自 {} 的訊息:{}".format(message.author, message.content))     
        if self.user.mentioned_in(message):
            logging.debug("Money被叫到了 ！")
            await message.channel.send(f"```{help_text}```")    
    
if __name__ == "__main__":
    '''
    Settings
    '''
    with open("./Money_add/account.info", "r", encoding="utf-8") as f:
        accountDICT = json.load(f) 
    articut = Articut(username=accountDICT["username"], apikey=accountDICT["api_key"])
    intents = discord.Intents.default()
    intents.message_content = True
    client = Client(command_prefix = "!", intents=intents)
    GUILD_ID = discord.Object(id = accountDICT["server_id"])

    @client.tree.command(name="add", description="新增紀錄", guild=GUILD_ID)
    @app_commands.describe(text="輸入至少含有事項、金額。例：10/11花了100元買蛋糕")    
    async def add_cmd(interaction: discord.Interaction, text: str):
        await interaction.response.defer(thinking=True, ephemeral=True)
        print(f"收到訊息。{text}")
        category = Category(interaction.user.name, interaction.user.id)
        record = Record(interaction.user.name, interaction.user.id)        
        try:           
            result = record.add(text, category, user_name = interaction.user.display_name)
            await interaction.followup.send(f"```{result}```")
        except Exception as e:
            logging.error(f"{e}")
            insertUtterance(
                username=accountDICT["username"], 
                lokiKey=accountDICT["loki_key"], 
                projectNameSTR="Money_add", 
                intentNameSTR="check", 
                utteranceLIST=[text]
            )                
            await interaction.followup.send(str(e))


        
    @client.tree.command(name="view", description="查看紀錄", guild=GUILD_ID)
    @app_commands.describe(text="選填，自動分析欲搜尋之時間、收支類別。例：10月的收入。去年花了多少錢吃東西")
    async def view_cmd(interaction: discord.Interaction, text: str = None):
        await interaction.response.defer(thinking=True, ephemeral=True)
        print(f"收到訊息。{text}")
        category = Category(interaction.user.name, interaction.user.id)
        record = Record(interaction.user.name, interaction.user.id)
        try:
            if text:
                result = record.search(text, category, user_name = interaction.user.display_name)
            else: 
                result = record.view(user_name = interaction.user.display_name)
    
            await interaction.followup.send(f"```{result}```")
        except Exception as e:
            await interaction.followup.send(f"{e}")

                
    @client.tree.command(name="report", description="回報錯誤", guild=GUILD_ID)
    @app_commands.describe(text="請輸入分析錯誤的句子（原句）", reason="請輸入錯誤原因或想要的正確結果")
    async def report_cmd(interaction: discord.Interaction, text: str, reason: str):
        await interaction.response.defer(thinking=True, ephemeral=True)
        print(f"收到訊息。原句：{text}，原因：{reason}")
        utterance = [f"原句：{text}，原因：{reason}"]
        insertUtterance(
            username=accountDICT["username"],
            lokiKey=accountDICT["loki_key"],
            projectNameSTR="Money_add",
            intentNameSTR="check",
            utteranceLIST= utterance
        )
    
        await interaction.followup.send(
            f"```已回報：\n原句：{text}\n原因：{reason}\n感謝您～```"
        )

    
    @client.tree.command(name="help", description="查看指令說明", guild=GUILD_ID)
    async def help_cmd(interaction: discord.Interaction):
        await interaction.response.defer(thinking=True, ephemeral=True)
        await interaction.followup.send(f"```{help_text}```")

    @client.tree.command(name="delete", description="刪除一筆紀錄", guild=GUILD_ID)
    @app_commands.describe(index="要刪除的紀錄編號（請先用 /view 查詢編號）")
    async def delete_cmd(interaction: discord.Interaction, index: int):
        await interaction.response.defer(thinking=True, ephemeral=True)
        print(f"收到訊息。{index}")
        record = Record(interaction.user.name, interaction.user.id)
        try:
            result = record.delete(index, user_name=interaction.user.display_name)
            await interaction.followup.send(f"```{result}```")
        except Exception as e:
            await interaction.followup.send(f"{e}")
    
    client.run(accountDICT["discord_token"])
