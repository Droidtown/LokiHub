#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint
from pycnnum import cn2num
#from ArticutAPI import Articut

#from <your_loki_main_program> import runLoki #放 Loki 主程式

logging.basicConfig(level=logging.DEBUG)


with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):
    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT 
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"gender": None,
                             "age":None,
                             "height":None,
                             "weight":None,
                             "BMR":None
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
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
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
                    replySTR = "為了計算基礎代謝率，需要請您提供您的生理性別 (請回答男或女)"


# ##########非初次對話：這裡用 Loki 計算語意 (真正的邏輯應該寫在這)
            else: #開始處理正式對話
                if msgSTR in ["男","女"]:
                    self.mscDICT[message.author.id]["gender"] = msgSTR
                    replySTR = "請您提供您的年齡 (請回答__歲)"
                    #if isinstance(int(msgSTR), int) == False:
                        #replySTR = cn2num(msgSTR) 轉數值
                elif re.search('(\d+)歲', msgSTR) != None:
                    user_age = re.search('(\d+)歲', msgSTR).group(1)
                    self.mscDICT[message.author.id]["age"] = user_age
                    replySTR = "請您提供您的身高 (請回答__公分)"
                        #if isinstance(int(msgSTR), int) == False:
                            #replySTR = cn2num(msgSTR)
                elif re.search('(\d+)公分', msgSTR) != None:
                    user_height = re.search('(\d+)公分', msgSTR).group(1)
                    self.mscDICT[message.author.id]["height"] = user_height
                    replySTR = "請您提供您的體重 (請回答__公斤)"
                elif re.search('(\d+)公斤', msgSTR) != None:
                    user_weight = re.search('(\d+)公斤', msgSTR).group(1)
                    self.mscDICT[message.author.id]["weight"] = user_weight
                    for i in self.mscDICT[message.author.id].values():
                        if i != None:
                            replySTR = self.mscDICT[message.author.id]["gender"] + ", " + self.mscDICT[message.author.id]["age"] + "歲" + ", " + self.mscDICT[message.author.id]["height"] + "公分" + ", " + self.mscDICT[message.author.id]["weight"] + "公斤" + "。" + "請確認您的資料是否正確" + "，" + "請回答是或否"
                elif msgSTR == "是":
                    if self.mscDICT[message.author.id]["gender"] == "男":
                        BMR = 66 + (13.7 * int(self.mscDICT[message.author.id]["weight"]) + 5 * int(self.mscDICT[message.author.id]["height"]) - 6.8 * int(self.mscDICT[message.author.id]["age"]))
                        self.mscDICT[message.author.id]["BMR"] = BMR
                        replySTR = "您的基礎代謝率為 " + str(self.mscDICT[message.author.id]["BMR"]) + " 卡"
                    if  self.mscDICT[message.author.id]["gender"] == "女":
                        BMR = 655 + (9.6 * int(self.mscDICT[message.author.id]["weight"]) + 1.8 * int(self.mscDICT[message.author.id]["height"]) - 4.7 * int(self.mscDICT[message.author.id]["age"]))
                        self.mscDICT[message.author.id]["BMR"] = BMR
                        replySTR = "您的基礎代謝率為 " + str(self.mscDICT[message.author.id]["BMR"]) + " 卡"
                elif msgSTR == "否":
                    replySTR = "為了更新您的資料，需要請您提供您的生理性別 (請回答男或女)"
                
                #從這裡開始接上 NLU 模型
                #resulDICT = getLokiResult(msgSTR) #Loki 回來的結果
                #logging.debug("######\nLoki 處理結果如下：") #寫 if else 問基本資訊
                #logging.debug(resulDICT)

        await message.reply(replySTR) #機器人統一回覆
        # if 欄位滿了，跳確認訊息
        print(self.mscDICT)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])