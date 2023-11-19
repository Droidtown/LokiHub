#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint

from condition import condition_control

logging.basicConfig(level=logging.DEBUG)

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID): # MSC = Multi section conversation多輪對話(不斷更新說話時間)
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "background":{
                                 "age":"None",
                                 "ten_month":"None",
                                 "weight":"None",
                                 "congenital_disease":"None",
                                 "genetic_disease":"None",
                             },
                             "environment":{
                                 "school":"None",
                                 "3c":"None"                                 
                             },
                             "behavior":{
                                 "q1":"None",
                                 "q2":"None",
                                 "q3":"None",
                                 "q4":"None",
                                 "q5":"None",
                                 "q6":"None",
                                 "q7":"None",
                                 "q8":"None",
                                 "q9":"None",
                                 "q10":"None",
                                 "q11":"None",
                                 "q12":"None",
                                 "q13":"None"
                             },
                             "a":False,
                             "b":False,
                             "c":False,
                             "response":[]
        }
        self.mscDICT = { "userid":self.templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user: #bot不會回自己
            return None
        print(message)
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            #msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            msgSTR = re.sub("<@\d+>\s?", "", message.content).strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:  #把英文字母收斂成小寫
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():  #直接去找之前是否有對話過
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[str(message.author.id)+":"+str(message.author)] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但其實我的記憶力跟金魚差不了多少，所以要重新開始問一次喔～\n我是線上語言能力篩檢助理機器人。我可以幫助你了解孩子的語言發展狀況。\n在此之前須要先知道一下孩子的基本訊息，請問他現在幾歲呢？" #可以自修改回應內容
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[str(message.author.id)+":"+str(message.author)]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[str(message.author.id)+":"+str(message.author)] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title() + "\n我是線上語言能力篩檢助理機器人。我可以幫助你了解孩子的語言發展狀況。在此之前須要先知道一下孩子的基本訊息，請問他現在多大了呢？"
# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                
                data_dict = self.mscDICT[str(message.author.id)+":"+str(message.author)]

                # 用檢查字典值a, b, c是否為True的方式確認應該進行哪個context
                if data_dict["a"] == False:
                    resultDICT = condition_control(data_dict, "background", msgSTR)
                    print(resultDICT)
                    self.mscDICT[str(message.author.id)+":"+str(message.author)]["background"].update(resultDICT) # 把判斷完的新資料更新進mscDICT
                    replySTR = self.mscDICT[str(message.author.id)+":"+str(message.author)]["background"]["response"]
                    # 確認 context a 資料是否蒐集完畢
                    if "a" in resultDICT.keys():
                        self.mscDICT[str(message.author.id)+":"+str(message.author)]["a"] = True
                elif data_dict["b"] == False:
                    resultDICT = condition_control(data_dict, "environment", msgSTR)
                    self.mscDICT[str(message.author.id)+":"+str(message.author)]["environment"].update(resultDICT) # 把判斷完的新資料更新進mscDICT
                    replySTR = resultDICT["response"]
                    if "b" in resultDICT.keys():
                        self.mscDICT[str(message.author.id)+":"+str(message.author)]["b"] = True
                elif data_dict["c"] == False:
                    age = data_dict["background"]["age"]
                    if age // 12 == 0:    
                        target_context = "under1"
                    else:
                        target_context = "above" + str(age//12)
                    resultDICT = condition_control(data_dict, target_context, msgSTR)
                    self.mscDICT[str(message.author.id)+":"+str(message.author)]["behavior"].update(resultDICT) # 把判斷完的新資料更新進mscDICT
                    replySTR = resultDICT["response"]
                    if "c" in resultDICT.keys():
                        self.mscDICT[str(message.author.id)+":"+str(message.author)]["c"] = True
                
                logging.debug("######\nLoki 處理結果如下：")
                # logging.debug(resultDICT)
            pprint(self.mscDICT[str(message.author.id)+":"+str(message.author)])
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
