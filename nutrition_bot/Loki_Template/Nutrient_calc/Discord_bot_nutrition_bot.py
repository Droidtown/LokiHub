#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import pandas as pd
from datetime import datetime
from pprint import pprint

from Nutrient_calc import runLoki
from exp_read_sheet import start_dri

logging.basicConfig(level=logging.DEBUG)

#with open("account.info", encoding="utf-8") as f: #讀取account.info
    #accountDICT = json.loads(f.read())


punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    refDICT = { 
        "age": [],
        "gen": [],
        "clf": [], 
        "meas": [],
        "food": [],
        "nutrient": []
    }    
    resultDICT = runLoki(inputLIST, filterLIST, refDICT)
    
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = {    "id": messageAuthorID,
                             "updatetime" : datetime.now(),
                             "latestQuest": "",
                             "false_count" : 0
        }
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": ""
        }
        self.mscDICT = {"age": None,
                        "gen": None,
                        "clf": None,
                        "meas": None,
                        "food": None,
                        "nutrient": None
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello", "hey"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    #timeReset = datetime.time(3,0,0,0, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
                    ##設定更新紀錄時間為台灣時區每天凌晨三點
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_secinds() >= 1800:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過30分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "嗨，我是你的營養計算小幫手，\n我可以幫你計算今天已經攝取的營養\n或是今天需要的營養(例：我今天需要攝取多少營養)"
    

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                nu_total = ["營養", "維生素A", "維生素D", "維生素E", "維生素K", "維生素C", "維生素B1", "維生素B2", "菸鹼素", "維生素B6", "維生素B12", "葉酸", "鈣", "磷", "鎂", "鐵", "鋅", "碘", "鉀", "鈉"]
                #if resultDICT["nutrient"][0] not in nu_total:
                    #print("got it!")
                    #resultDICT["nutrient"] = []
                    #replySTR = "我們目前沒有提供該營養素的計算喔！您可以詢問的有：{}".format("維生素A, 維生素D, 維生素E, 維生素K, 維生素C, 維生素B1, 維生素B2, 菸鹼素, 維生素B6, 維生素B12, 葉酸, 鈣, 磷, 鎂, 鐵, 鋅, 碘, 鉀, 鈉")
                
                if len(resultDICT["nutrient"]) != 0:
                    self.mscDICT["nutrient"] = resultDICT["nutrient"][0].upper()
                    replySTR = "請輸入年齡（如：10歲）"                
                elif len(resultDICT["age"]) != 0:
                    self.mscDICT["age"] = resultDICT["age"][0]
                    replySTR = "請輸入性別（如：女生）"
                else: #len(resultDICT["gen"]) != 0:
                    self.mscDICT["gen"] = resultDICT["gen"][0]
                    if self.mscDICT["nutrient"] == "營養":
                        ret = start_dri(self.mscDICT["age"], self.mscDICT["gen"], self.mscDICT["nutrient"])
                        out_str = str()
                        for ind, value in ret.items():
                            out_str = out_str + ind + " : " + value + "\n"
                        replySTR = "好的！您的資訊如下(年齡：{0}、性別：{1})\n您一天所需的營養為：\n{2}".format(self.mscDICT["age"], self.mscDICT["gen"], out_str)
                    else:
                        replySTR = "好的！您的資訊如下(年齡：{0}、性別：{1}、營養素：{2})\n您一天所需的營養為：\n{3}: {4} {5}".format(self.mscDICT["age"], self.mscDICT["gen"], self.mscDICT["nutrient"], self.mscDICT["nutrient"], start_dri(self.mscDICT["age"], self.mscDICT["gen"], self.mscDICT["nutrient"])[0], start_dri(self.mscDICT["age"], self.mscDICT["gen"], self.mscDICT["nutrient"])[1])              
                
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
