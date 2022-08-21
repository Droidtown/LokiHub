#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import os, sys
import csv

# 設定路徑
path_current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(path_current))
os.chdir(path_current)

from SpendThrift_bot import runLoki
from datetime import datetime
from pprint import pprint

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


logging.basicConfig(level=logging.DEBUG)

# 讀取 account.info，取得 discord bot 的 token
with open(path_current + "/account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())


# 用標點符號做斷句
punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+") # TODO: 不知道為甚麼要在做一次= =
    
    # 將輸入斷句
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    
    # 篩選條件
    filterLIST = []
    
    # 送進 Loki 理做判斷
    resultDICT = runLoki(inputLIST, filterLIST)
    
    # 顯示結果
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
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": ""
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None
        
        # 如果 server 中的所有 bot 被點名，回答
        elif message.content.lower().replace(" ", "") in ("bot點名"): 
            await message.reply("有！")     # TODO: 敗家子 style


        # 顯示是哪個使用者傳了什麼訊息
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))


        # 如果 bot 有被 @ 到        
        if "<@!{}>".format(self.user.id) in message.content or "<@{}>".format(self.user.id) in message.content: # (client.user.id) is botID
            # 消除 @ bot 的文字內容
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            
            # 顯示剩餘訊息
            logging.debug("本 bot 被叫到了！")
            logging.debug("人類說：{}".format(msgSTR))

            print("here")


            # 特殊指令，套用自定義回應
            if msgSTR == "ping":
                await message.reply('pong')
            elif msgSTR == "ping ping":
                await message.reply('pong pong')
# ##########初次對話：這裡是 keyword trigger 的。

            # 如果在跟 bot 打招呼
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title()

# ##########非初次對話：這裡用 Loki 計算語意            
            else: #開始處理正式對話，開始接上 NLU 模型
                resulDICT = runLoki([msgSTR])
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resulDICT)
                print(resulDICT)
                
                
                # TODO: 針對不同種類的意圖，做出不同的回覆：
                # Our Code here...
                    
            # 判斷完畢，回覆使用者
            await message.reply(replySTR)


# 啟動 bot
if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])
