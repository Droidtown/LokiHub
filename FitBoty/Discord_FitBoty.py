#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import datetime
import discord
import json
import re
from pprint import pprint
from pycnnum import cn2num
from ArticutAPI import Articut

from FitBoty import runLoki #放 Loki 主程式

logging.basicConfig(level=logging.DEBUG)


with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])

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
                             "BMR":None,
                             "food_cal":None,
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
        elif message.content.lower().replace(" ", "") in ("bot點名"):
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
                print(resultDICT)#Loki 回來的結果
                for i in resultDICT.keys():
                    if i == "gender":
                        self.mscDICT[message.author.id]["gender"] = resultDICT["gender"]
                        replySTR = "你今年幾歲呢？"
                    if i == "age":
                        self.mscDICT[message.author.id]["age"] = resultDICT["age"]
                        replySTR = "你身高幾公分？"
                        
                    if i == "height":
                        self.mscDICT[message.author.id]["height"] = resultDICT["height"]
                        replySTR = "你體重幾公斤？"
                    
                    if i == "weight":
                        self.mscDICT[message.author.id]["weight"] = resultDICT["weight"]
                        for i in self.mscDICT[message.author.id].values():
                            if i != None:
                                replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + self.mscDICT[message.author.id]["age"] + "歲" + "\n" + self.mscDICT[message.author.id]["height"] + "公分" + "\n" + self.mscDICT[message.author.id]["weight"] + "公斤" + "\n" + "請確認以上資料是否正確？"


                if msgSTR.lower() in ["是","對","是的","對的","沒錯","正確","yes"]:
                    if self.mscDICT[message.author.id]["gender"] == "男性":
                        BMR = 66 + (13.7 * int(self.mscDICT[message.author.id]["weight"]) + 5 * int(self.mscDICT[message.author.id]["height"]) - 6.8 * int(self.mscDICT[message.author.id]["age"]))
                        #self.mscDICT[message.author.id]["BMR"] = BMR
                        await message.reply("你的基礎代謝率為 " + str(BMR) + " 卡" + "。")
                        self.mscDICT[message.author.id]["BMR"] = BMR
                    if  self.mscDICT[message.author.id]["gender"] == "女性":
                        BMR = 655 + (9.6 * int(self.mscDICT[message.author.id]["weight"]) + 1.8 * int(self.mscDICT[message.author.id]["height"]) - 4.7 * int(self.mscDICT[message.author.id]["age"]))
                        self.mscDICT[message.author.id]["BMR"] = BMR
                        await message.reply("你的基礎代謝率為 " + str(self.mscDICT[message.author.id]["BMR"]) + " 卡" + "。")
                elif msgSTR.lower() in ["否","錯","有錯","錯誤","no"]:
                    replySTR = "為了更新您的資料，需要請你提供你的生理性別"

                if self.mscDICT[message.author.id]["BMR"] != None:
                    if int(datetime.datetime.now().strftime('%H')) < 12:
                        replySTR = "你早餐吃了什麼呢？"
                    elif int(datetime.datetime.now().strftime('%H')) > 12 and int(datetime.datetime.now().strftime('%H')) < 19:
                        replySTR = "你早餐和午餐吃了什麼呢？"
                    elif int(datetime.datetime.now().strftime('%H')) > 19:
                        replySTR = "你今天三餐吃了些什麼呢？"
                
                for i in resultDICT.keys():
                    if i == "food_cal":
                        self.mscDICT[message.author.id]["food_cal"] = resultDICT["food_cal"]
                        replySTR = "總共" + str(self.mscDICT[message.author.id]["food_cal"]) + "卡"
                
                
                
                
                logging.debug("######\nLoki 處理結果如下：") 
                logging.debug(resultDICT)
                

        await message.reply(replySTR) #機器人統一回覆
        print(self.mscDICT)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])