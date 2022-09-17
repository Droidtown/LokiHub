#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from random import choice
from pprint import pprint
from datetime import datetime
from rockClimbing import runLoki
from rockClimbingNLUmodel import NLUmodel

logging.basicConfig(level=logging.DEBUG)

with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID): #清空與 messageAuthorID 之間的對話記錄
        logging.info("\n--reset message--")
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        self.templateDICT = {"updatetime": None,
                             "latestQuest": "",
                             "replySTR":"",
                             "msgSTR":"",
                             "_gym_time":"",
                             "_person_loc":"",
                             "_day_of_week": "",
                             "_gym_name":"",
                             "_rock_climbing":"",
                             "_distance_intent":0,
        }
        self.templateDICT["_day_of_week"] = datetime.today().weekday()
        self.mscDICT = { 
        }
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        if message.author == self.user:
            return None
        
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):#if "<@!{}>".format(self.user.id) in message.content or "<@{}>".format(self.user.id) in message.content:#
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("本 bot 被叫到了！")
            logging.debug("人類說：{}".format(msgSTR))

            # keyword trigger 打招呼 
            if msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello","妳好","嗨嗨","安安","hey","yo","阿羅哈","你好啊","你好呀"]:
                logging.debug("msgSTR1:{}\n".format(msgSTR))
                #有講過話(判斷對話時間差)
                print("message.author.id = {}".format(message.author.id))
                print("self.mscDICT.keys() =",self.mscDICT.keys())
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    if timeDIFF.total_seconds() >= 300: #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        self.mscDICT[message.author.id]["replySTR"] = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    else:#有講過話，而且還沒超過5分鐘就又hello 
                        self.mscDICT[message.author.id]["replySTR"] = msgSTR.title() #self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    print("message.author.id = {}".format(message.author.id))
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    self.mscDICT[message.author.id]["replySTR"] = "哈囉！我是你的攀岩知識小幫手～\n幫你解決對攀岩的各種疑惑！\n有什麼想問的呢？"#msgSTR.title()
            elif "感謝" in msgSTR.lower() or "謝謝" in msgSTR.lower()  or "感恩" in msgSTR.lower() or "thank" in msgSTR.lower() or "tks" in msgSTR.lower() or "thx" in msgSTR.lower():
                if message.author.id not in self.mscDICT.keys():
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    self.mscDICT[message.author.id]["replySTR"] = "謝啥呢？都還沒問問題呢！"
                else:
                    self.mscDICT[message.author.id]["replySTR"] = choice(["不客氣！","不客氣哦！隨時歡迎再問我問題～","不會！還有什麼攀岩相關問題都歡迎提問哦:)"])
            else: #開始處理正式對話，接上 NLU 模型
                print("msgSTR2:",msgSTR,)
                print(self.mscDICT.keys())
                if message.author.id not in self.mscDICT.keys():
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                self.mscDICT[message.author.id]["msgSTR"] = msgSTR #將取回的資訊 update 到人類的 msc 裡。
                self.mscDICT[message.author.id] = NLUmodel(self.mscDICT[message.author.id])
<<<<<<< HEAD
            print('\n---message reply：',self.mscDICT[message.author.id]["replySTR"],"---\n")
            await message.reply(self.mscDICT[message.author.id]["replySTR"])
=======
        
        await message.reply(self.mscDICT[message.author.id]["replySTR"])
>>>>>>> 89dfbbc34e4b68876a0a912abc868a4b4f5d1ac4


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])
