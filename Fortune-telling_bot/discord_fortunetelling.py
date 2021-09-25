#!/user/bin/env python
# -*- coding: utf-8 -*-
import logging
import discord
import time
import datetime
import json
import re
import random
import pandas as pd
import pprint
from fortunetelling import runLoki

logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()
processTemplate={"ask":"",
                 "wish":"",
                 "updatetime":None}
mscDICT = {}

with open("account.txt", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n") #斷句
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT


@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))
    
@client.event
async def on_message(message):
    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return
    
    print("message.author =", message.author, "\nmessage.content =", message.content)
    msgSTR = re.sub("<@[!&]{}> ?".format(message.author), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    if re.search("(hi|hello|哈囉|嗨|[你您]好|hola)", msgSTR.lower()): #可以增加啟動呼叫方式
        if message.author in mscDICT.keys():
            now_datetime = datetime.datetime.now()
            mscDICT[message.author]["first_time"]=mscDICT[message.author]["second_time"]
            time_diff = now_datetime - mscDICT[message.author]["first_time"]
            if time_diff.total_seconds() >= 180:
                replySTR = """Hi!你好，我是易經占卜師。我擅長幫人家占卜運勢、愛情、求職、事業、考試等問題。
                              不知道你最近有什麼煩惱嗎？不妨和我說說，我可以給你一些占卜上的建議唷！""".replace(" ", "")
                await message.reply(replySTR)
                del mscDICT[message.author]
                mscDICT[message.author]["first_time"] = datetime.datetime.now()
                mscDICT[message.author]["second_time"] = datetime.datetime.now()
                mscDICT[message.author]["repeat"] = ""                
                return
            elif (time_diff.total_seconds() < 180) and (mscDICT[message.author]["repeat"]=="yes"):                
                replySTR = """Hi!你好，我是易經占卜師。我擅長幫人家占卜運勢、愛情、求職、事業、考試等問題。
                              不知道你最近有什麼煩惱嗎？不妨和我說說，我可以給你一些占卜上的建議唷！""".replace(" ", "")
                await message.reply(replySTR)
                mscDICT[message.author]["repeat"]=""
                
                return
            elif ("process" in mscDICT[message.author]) and (mscDICT[message.author]["process"] != {}):
                await message.reply("你還沒和上天說出祈求的話語唷")
                return
            else:
                await message.reply("你還沒有說出你最近的煩惱唷！")
                return
        else:
            replySTR = """Hi!你好，我是易經占卜師。我擅長幫人家占卜運勢、愛情、求職、事業、考試等問題。
                          不知道你最近有什麼煩惱嗎？不妨和我說說，我可以給你一些占卜上的建議唷！""".replace(" ", "")
            await message.reply(replySTR)
            mscDICT[message.author]={"first_time":datetime.datetime.now(),"second_time":datetime.datetime.now(),"repeat":""}
            return        
    
    if message.author not in mscDICT.keys():
        mscDICT[message.author]={}
        mscDICT[message.author]["second_time"] = datetime.datetime.now()
        mscDICT[message.author]["repeat"]=""        
    
    if "process" not in mscDICT[message.author]:     # 判斷 User 是否為第一輪對話
        mscDICT[message.author]["process"]={}
        mscDICT[message.author]["first"]="no"
        mscDICT[message.author]["completed"]=False
        lokiResultDICT = getLokiResult(msgSTR)
        if lokiResultDICT == {}:
            await message.reply("你的問題可能不是我的專長領域，又或者是你說明得不夠清楚。\n再麻煩你說明得清楚一些，好讓我理解，謝謝！\n另外，你也可以直接說你想算哪個方面，可以更快更精準讓我知道唷！")
            del mscDICT[message.author]["process"]
            del mscDICT[message.author]["first"]
            del mscDICT[message.author]["completed"]
            return
        else:
            mscDICT[message.author]["process"] = lokiResultDICT
            if mscDICT[message.author]["first"] =="no" :    #多輪對話的問句。
                if "wish" not in mscDICT[message.author]["process"]:
                    replySTR = """我了解你的問題了，接下來我會帶領你進行占卜。
                                  首先，先請你虔誠的向上天或者是神明說出祈求的話語！""".replace(" ", "")
                    await message.reply(replySTR)
                    mscDICT[message.author]["process"]["wish"]=""
                    return

    mscDICT[message.author]["process"]["wish"]=msgSTR
            
            
                    
    if mscDICT[message.author]["process"]["wish"]!="":
        num1=random.randint(1,2)
        num2=random.randint(1,2)
        num3=random.randint(1,2)
        num4=random.randint(1,2)
        num5=random.randint(1,2)
        num6=random.randint(1,2)
        gua=int(str(num6)+str(num5)+str(num4)+str(num3)+str(num2)+str(num1))
        #pic1=image.File('C:\Users\User\Documents\GitHub\fortune-telling\陽爻.png')
        #pic2=picture.File('C:\Users\User\Documents\GitHub\fortune-telling\陰爻.png')
        data = pd.read_csv('卜卦機器人資料庫.csv',encoding='utf-8')
        for i in range(0,64):
            if gua == data.iloc[i,0]:
                replySTR="""好的，占卜的結果出來囉！你所卜出來的卦是「{}」卦，在此給你一些小建議：
                            {}
                                
                            另外，你所煩惱的面向是關於「{}」，而根據占卜的結果顯示：
                            {}
                            """.format(data.iloc[i,2],
                                       data.iloc[i,4],
                                       mscDICT[message.author]["process"]["ask"],
                                       data.iloc[i][mscDICT[message.author]["process"]["ask"]]).replace(" ", "")
                await message.reply(replySTR)
        mscDICT[message.author]["completed"] = True
                    
    print("mscDICT =",mscDICT)
                    
    if mscDICT[message.author]["completed"]:    # 清空 User Dict
        del mscDICT[message.author]
        mscDICT[message.author] = {"second_time":datetime.datetime.now(),"repeat":"yes"}
        
    return                    
                    
                    
if __name__ == "__main__":
    client.run(accountDICT["discord_token"])
        
            
        
        
