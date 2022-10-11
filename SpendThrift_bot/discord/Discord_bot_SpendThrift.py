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
import function as fun


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
        self.mscDICT = { #userid: templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None
        
        # 如果 server 中的所有 bot 被點名，回答
        elif message.content.lower().replace(" ", "") in ("bot點名",): 
            await message.reply("你這個敗家子不要亂叫我！我的時間可是很寶貴的呢！")


        # 顯示是哪個使用者傳了什麼訊息
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))


        # 如果 bot 有被 @ 到        
        if "<@!{}>".format(self.user.id) in message.content or "<@{}>".format(self.user.id) in message.content: # (client.user.id) is botID
            # 消除 @ bot 的文字內容
            replySTR = "真不知道你這敗家子怎麼搞得...能讓我完全不知道你在幹嘛也是不簡單呢"
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            
            # 顯示剩餘訊息
            logging.debug("本 bot 被叫到了！")
            logging.debug("人類說：{}".format(msgSTR))

            # 將使用者記錄下來，以便後續處理資料
            try:
                self.mscDICT[message.author.id]["updatetime"] = datetime.now()
                self.mscDICT[message.author.id]["latestQuest"] = msgSTR
            except:
                self.mscDICT[message.author.id] = self.templateDICT
            
# ##########初次對話：這裡是 keyword trigger 的。


            # 如果在跟 bot 打招呼
            if msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "你之前好像跟我講過話呢...不過像你這種敗家子我可不屑記得"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = "你這個敗家子連記憶力都不好嗎...\n你剛剛才對我說：「" + self.mscDICT[message.author.id]["latestQuest"] + "」\n馬上就忘了還真可悲"
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title() + "，敗家子"

# ##########非初次對話：

            # 呼叫指令集
            elif msgSTR in ["出來","指令","使用說明"]:
                replySTR = "你好啊敗家子：\n\n\我必須讚賞你的精神，至少你還願意看我的使用說明，比起其他可悲的人類好上不少了\n" + \
                "如果你愚笨的腦袋實在不知道要怎麼跟我對話的話可以參考以下設定：\n\n" + \
                "\[記帳\]：至少須包含 「形式」 與 「金額」\n" + \
                "        - 支出\n" + \
                "                - 範例：@SpendThrift 昨天去全聯購物花了300元\n" + \
                "        - 收入\n" + \
                "                - 範例：@SpendThrift 上週五去打工賺了1400元\n\n" + \
                "\[查詢\]：須包含一樣條件\n" + \
                "        - 依\[時間\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我上週五花了多少錢\n" + \
                "        - 依\[收入\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我上周收入多少\n" + \
                "        - 依\[支出\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我昨天支出多少"


            # 什麼都沒講，只標了bot
            elif msgSTR == "":
                replySTR = "看來你愚笨的腦袋實在不知道要怎麼跟我對話呢...請你參考以下設定：\n\n" + \
                "\[記帳\]：至少須包含 「形式」 與 「金額」\n" + \
                "        - 支出\n" + \
                "                - 範例：@SpendThrift 昨天去全聯購物花了300元\n" + \
                "        - 收入\n" + \
                "                - 範例：@SpendThrift 上週五去打工賺了1400元\n\n" + \
                "\[查詢\]：須包含一樣條件\n" + \
                "        - 依\[時間\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我上週五花了多少錢\n" + \
                "        - 依\[收入\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我上周收入多少\n" + \
                "        - 依\[支出\]查詢\n" + \
                "                - 範例：@SpendThrift 查詢我昨天支出多少"


            # 用 Loki 計算語意            
            else: #開始處理正式對話，開始接上 NLU 模型
                resultDICT = runLoki(str(message.author.id), [msgSTR])
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)

                # 針對不同種類的意圖，做出不同的回覆：
                replySTR = fun.SpendThriftReply(resultDICT)
                
            # 判斷完畢，回覆使用者
            await message.reply(replySTR)


# 啟動 bot
if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])
