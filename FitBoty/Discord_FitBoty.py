#!/user/bin/env python
# -*- coding: utf-8 -*-

from ArticutAPI import Articut
import cn2num
import datetime
import discord
from FitBoty import runLoki
import json
import logging
from pprint import pprint
import re


logging.basicConfig(level=logging.DEBUG)


with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])

with open("sports_dict.json", encoding="utf-8") as f: #讀取account.info
    sports_dict = json.loads(f.read())

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result

class BotClient(discord.Client):
    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT 
        templateDICT["updatetime"] = datetime.datetime.now()
        return templateDICT

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"gender": None,
                             "age":None,
                             "height":None,
                             "weight":None,
                             "correct":None,
                             "incorrect":None,
                             "BMR":None,
                             "food_cal":None,
                             "sports_cal":None,
                             "updatetime": datetime.datetime.now()
        }
        self.mscDICT = {
                         
        }
        # ####################################################################################

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user: #message 是 human，user 是 bot
            return None
        elif message.content.lower().replace(" ", "") in ("bot點名",):
            await message.reply("有！")

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping": #用以測試 bot 是否可執行
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR="pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","安安","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    await message.reply("嗨嗨我是 FitBoty :)")
                    replySTR = "我會計算你每日攝取熱量與基礎代謝率之差值，並推薦你適合的運動項目。\n為了計算你的基礎代謝率，想請問你的生理性別是？"


# ##########非初次對話：這裡用 Loki 計算語意 (真正的邏輯應該寫在這)
            else: #開始處理正式對話
                
                        #use datetime to get current time.
                        #if before 12:00pm, ask breakfast
                        #if between 12pm to 7pm, ask breakfast and lunch
                        #if after 7pm, ask what are eaten in this day
                
                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR)
                print(resultDICT) #Loki 回來的結果
                if re.search("男|男生|男性|男人|男子|帥哥|大叔|先生|歐巴", msgSTR) != None and re.search("不", msgSTR) == None:
                    self.mscDICT[message.author.id]["gender"] = "男性"
                    replySTR = "你今年幾歲呢？"
                    
                elif re.search("女|女生|女人|女性|女子|美女|小姐|阿姨|大嬸", msgSTR) != None and re.search("不", msgSTR) == None:
                    self.mscDICT[message.author.id]["gender"] = "女性"
                    replySTR = "你今年幾歲呢？"
                else:
                    for i in resultDICT.keys():
                        if i == "gender":
                            self.mscDICT[message.author.id]["gender"] = resultDICT["gender"]
                            self.mscDICT[message.author.id].update({"correct": None})
                            replySTR = "你今年幾歲呢？"

                if re.search("\d{3}", msgSTR) != None:
                    if self.mscDICT[message.author.id]["height"] !=None:
                        if re.search("\d+公斤", msgSTR) == None:
                            nmsgSTR = re.sub("(\d+)", r"\1公斤", msgSTR)
                            resultDICT = getLokiResult(nmsgSTR)
                            for i in resultDICT.keys():
                                if i == "weight":
                                    self.mscDICT[message.author.id]["weight"] = resultDICT["weight"]
                                    for i in self.mscDICT[message.author.id].values():
                                        if i != None:
                                            replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"                        
                    else: 
                        if re.search("\d+公分", msgSTR) == None:
                            nmsgSTR = re.sub("(\d+)", r"\1公分", msgSTR)
                            resultDICT = getLokiResult(nmsgSTR)
                            for i in resultDICT.keys():
                                if i == "height":
                                    self.mscDICT[message.author.id]["height"] = resultDICT["height"]
                                    replySTR = "你體重幾公斤？"
                        elif re.search("\d+CM|\d+cm|\d+Cm", msgSTR) != None:
                            nmsgSTR = re.sub("(\d+)", r"\1公分", msgSTR)
                            resultDICT = getLokiResult(nmsgSTR)
                            for i in resultDICT.keys():
                                if i == "height":
                                    self.mscDICT[message.author.id]["height"] = resultDICT["height"]
                                    replySTR = "你體重幾公斤？"
                        else:
                            for i in resultDICT.keys():
                                if i == "height":
                                    self.mscDICT[message.author.id]["height"] = resultDICT["height"]
                                    replySTR = "你體重幾公斤？"

                if re.search("\d{2}", msgSTR) != None:
                    if self.mscDICT[message.author.id]["age"] != None:
                        if len(msgSTR) == 2:
                            if re.search("\d+公斤", msgSTR) == None:
                                nmsgSTR = re.sub("(\d+)", r"\1公斤", msgSTR)
                                resultDICT = getLokiResult(nmsgSTR)
                                for i in resultDICT.keys():
                                    if i == "weight":
                                        self.mscDICT[message.author.id]["weight"] = resultDICT["weight"]
                                        for i in self.mscDICT[message.author.id].values():
                                            if i != None:
                                                replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"
                        elif re.search("\d+KG|\d+kg|\d+Kg", msgSTR) != None:
                            nmsgSTR = re.sub("(\d+)", r"\1公斤", msgSTR)
                            resultDICT = getLokiResult(nmsgSTR)
                            for i in resultDICT.keys():
                                if i == "weight":
                                    self.mscDICT[message.author.id]["weight"] = resultDICT["weight"]
                                    for i in self.mscDICT[message.author.id].values():
                                        if i != None:
                                            replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"
                        elif re.search("\d+公斤", msgSTR) != None:
                            for i in resultDICT.keys():
                                if i == "weight":
                                    self.mscDICT[message.author.id]["weight"] = resultDICT["weight"]
                                    for i in self.mscDICT[message.author.id].values():
                                        if i != None:
                                            replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"
                    else:
                        if re.search("\d+歲", msgSTR) == None:
                            nmsgSTR = re.sub("(\d+)", r"\1歲", msgSTR)
                            resultDICT = getLokiResult(nmsgSTR)
                            for i in resultDICT.keys():
                                if i == "age":
                                    self.mscDICT[message.author.id]["age"] = resultDICT["age"]
                                    replySTR = "你身高幾公分？"
                                    
                        elif re.search("\d+歲", msgSTR) != None:
                            for i in resultDICT.keys():
                                if i == "age":
                                    self.mscDICT[message.author.id]["age"] = resultDICT["age"]
                                    replySTR = "你身高幾公分？"
                else: 
                    if re.search("歲", msgSTR) !=None:
                        nmsgSTR = re.sub("歲","",msgSTR)
                        tmsgSTR = cn2num.transform(nmsgSTR)
                        self.mscDICT[message.author.id]["age"] = str(int(tmsgSTR))
                        replySTR = "你身高幾公分？"
                    elif re.search("公斤", msgSTR) !=None:
                        nmsgSTR = re.sub("公斤","",msgSTR)
                        tmsgSTR = cn2num.transform(nmsgSTR)
                        self.mscDICT[message.author.id]["weight"] = str(int(tmsgSTR))
                        for i in self.mscDICT[message.author.id].values():
                            if i != None:
                                replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"                        
                    elif re.search("公分",msgSTR) !=None:
                        nmsgSTR = re.sub("公分","",msgSTR)
                        tmsgSTR = cn2num.transform(nmsgSTR)
                        self.mscDICT[message.author.id]["height"] = str(int(tmsgSTR))
                        replySTR = "你體重幾公斤？"
                    elif cn2num.transform(msgSTR) != 0.0:
                        if self.mscDICT[message.author.id]["age"] != None and self.mscDICT[message.author.id]["height"] == None:
                            nmsgSTR = cn2num.transform(msgSTR)
                            self.mscDICT[message.author.id]["height"] = str(int(nmsgSTR))
                            replySTR = "你體重幾公斤？"
                        elif self.mscDICT[message.author.id]["height"] !=None:
                            nmsgSTR = cn2num.transform(msgSTR)
                            self.mscDICT[message.author.id]["weight"] = str(int(nmsgSTR))
                            for i in self.mscDICT[message.author.id].values():
                                if i != None:
                                    replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"                                   
                        else:
                            nmsgSTR = cn2num.transform(msgSTR)
                            self.mscDICT[message.author.id]["age"] = str(int(nmsgSTR)) 
                            replySTR = "你身高幾公分？"

                if self.mscDICT[message.author.id]["weight"] != None:
                    resultDICT = getLokiResult(msgSTR)
                    for i in resultDICT.keys():
                        if i == "correct":
                            self.mscDICT[message.author.id]["correct"] = resultDICT["correct"]
                            if self.mscDICT[message.author.id]["gender"] == "男性":
                                BMR = 66 + (13.7 * int(self.mscDICT[message.author.id]["weight"]) + 5 * int(self.mscDICT[message.author.id]["height"]) - 6.8 * int(self.mscDICT[message.author.id]["age"]))
                                await message.reply("你的基礎代謝率為 " + str(BMR) + " 卡" + "。")
                                self.mscDICT[message.author.id]["BMR"] = BMR
                            if  self.mscDICT[message.author.id]["gender"] == "女性":
                                BMR = 655 + (9.6 * int(self.mscDICT[message.author.id]["weight"]) + 1.8 * int(self.mscDICT[message.author.id]["height"]) - 4.7 * int(self.mscDICT[message.author.id]["age"]))
                                self.mscDICT[message.author.id]["BMR"] = BMR
                                await message.reply("你的基礎代謝率為 " + str(self.mscDICT[message.author.id]["BMR"]) + " 卡" + "。")

                        elif i == "incorrect":
                            self.mscDICT[message.author.id]["incorrect"] = resultDICT["incorrect"]
                            self.mscDICT[message.author.id].update({"gender": None, "age": None, "height": None, "weight": None})
                            replySTR = "為了更新你的資料，需要請你提供你的生理性別"


                if self.mscDICT[message.author.id]["BMR"] != None and self.mscDICT[message.author.id]["food_cal"] == None:
                    if int(datetime.datetime.now().strftime('%H')) >= 5 and int(datetime.datetime.now().strftime('%H')) < 12:
                        replySTR = "你早餐吃了什麼呢？"
                    elif int(datetime.datetime.now().strftime('%H')) >= 12 and int(datetime.datetime.now().strftime('%H')) < 19:
                        replySTR = "你早餐和午餐吃了什麼呢？"
                    elif int(datetime.datetime.now().strftime('%H')) >= 19 and int(datetime.datetime.now().strftime('%H')) <= 23:
                        replySTR = "你今天三餐吃了些什麼呢？"
                    elif int(datetime.datetime.now().strftime('%H')) >= 0 or int(datetime.datetime.now().strftime('%H')) < 5:
                        replySTR = "消夜吃了什麼呢？"
                
                if self.mscDICT[message.author.id]["BMR"] != None:
                    resultDICT = getLokiResult(msgSTR)                 
                    for i in resultDICT.keys():
                        if i == "food_cal":
                            self.mscDICT[message.author.id]["food_cal"] = sum(resultDICT["food_cal"])
                            if self.mscDICT[message.author.id]["food_cal"] == 0:
                                replySTR = "很抱歉，我無法估計你的進食熱量，在此先以 0 卡計算" + "。\n" + "請問你今天做了什麼運動且做了多久呢？"
                            else:
                                replySTR = "總共攝入" + str(self.mscDICT[message.author.id]["food_cal"]) + "卡" + "。\n" + "請問你今天做了什麼運動且做了多久呢？"
                                
                        if i == "sports_cal":
                            try:
                                self.mscDICT[message.author.id]["sports_cal"] = sum(resultDICT["sports_cal"])
                                if self.mscDICT[message.author.id]["sports_cal"] == int("0"):
                                    today_cal = float(self.mscDICT[message.author.id]["BMR"]) - float(self.mscDICT[message.author.id]["food_cal"])
                                    await message.reply("很抱歉，我無法估計你的運動熱量，在此先以 0 卡計算。")
                                else:
                                    today_cal = float(self.mscDICT[message.author.id]["BMR"]) - float(self.mscDICT[message.author.id]["food_cal"]) + float(self.mscDICT[message.author.id]["sports_cal"])
                                
                                sports_keyLIST = list(sports_dict.keys())
                                sports_valLIST = list(sports_dict.values())                        
                                if today_cal >= 0:
                                    rec_sportsSTR = '、'.join([str(s) for s in sports_keyLIST])
                                    replySTR = "你今日多消耗了" + str(today_cal) + "卡。\n恭喜你離你的目標又更近了一步！如果還有餘力，也推薦你可以做以下運動喔：\n" + rec_sportsSTR + "任一項進行10分鐘。"
                                else:
                                    rec_sportsLIST1 = []
                                    rec_sportsLIST2 = []
                                    rec_sportsLIST3 = []
                                    rec_sportsLIST4 = []
                                    for j in sports_valLIST:
                                        if today_cal*-1 <= j*10:
                                            rec_sports1 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports1:
                                                rec_sportsLIST1.append(i)                                        
                                        else:
                                            pass
                                        if today_cal*-1 > j*10 and today_cal*-1 <= j*20:
                                            rec_sports2 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports2:
                                                rec_sportsLIST2.append(i)    
                                        else:
                                            pass
                                        if today_cal*-1 > j*20 and today_cal*-1 <= j*30:
                                            rec_sports3 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports3:
                                                rec_sportsLIST3.append(i)    
                                        else:
                                            pass  
                                        if today_cal*-1 > j*30:
                                            rec_sports4 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports4:
                                                rec_sportsLIST4.append(i)                                    
                                        else:
                                            pass                                 
                                        
                                    if rec_sportsLIST1 != []:
                                        rec_sportsSTR1 = '、'.join([str(s) for s in set(rec_sportsLIST1)])
                                        rec_10min = rec_sportsSTR1 + "任一項進行10分鐘。\n"
                                    else: 
                                        rec_10min = ""
                                    if rec_sportsLIST2 != []:
                                        rec_sportsSTR2 = '、'.join([str(s) for s in set(rec_sportsLIST2)])
                                        rec_20min = rec_sportsSTR2 + "任一項進行20分鐘。\n"
                                    else: 
                                        rec_20min = ""                        
                                    if rec_sportsLIST3 != []:
                                        rec_sportsSTR3 = '、'.join([str(s) for s in set(rec_sportsLIST3)])
                                        rec_30min = rec_sportsSTR3 + "任一項進行30分鐘。\n"
                                    else: 
                                        rec_30min = ""
                                    if rec_sportsLIST4 != []:
                                        rec_sportsSTR4 = '、'.join([str(s) for s in set(rec_sportsLIST4)])
                                        rec_50min = rec_sportsSTR4 + "任一項進行50分鐘。\n"
                                    else: 
                                        rec_50min = ""                            
                                        
                                    replySTR = "你今日剩餘熱量為" + str(today_cal) + "卡。\n推薦你可以做以下運動消耗今日所剩的熱量喔：\n" + rec_10min + rec_20min + rec_30min + rec_50min 
                            except TypeError:
                                print("sportcal type error")
                                pass


                
                logging.debug("######\nLoki 處理結果如下：") 
                logging.debug(resultDICT)
                


        await message.reply(replySTR) #機器人統一回覆
        print(self.mscDICT)


if __name__ == "__main__":
    #client = BotClient()
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])