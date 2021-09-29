#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import json
from requests import post
from requests import codes
import math
from FearGreed_Bot import runLoki
from intent import Loki_ExtremeFear
from intent import Loki_Fear
from intent import Loki_Greed
from intent import Loki_Neutral
from intent import Loki_ExtremeGreed


with open("account.info.json",encoding="utf-8")as f :
    accountDICT=json.loads(f.read())

class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg == 'ping':
                await message.reply('pong')
            elif msg == 'ping ping':
                await message.reply('pong pong')
            elif msg == 'hi':
                await message.reply('哈囉我是FearGreed_Bot')
                
            
                
            else:
                #從這裡開始接上 NLU 模型


                responseLIST = ["我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"]

                inputLIST = [msg]
                filterLIST = []
                resultDICT = runLoki(inputLIST, filterLIST)
                print("Result => {}".format(resultDICT))

                indexSTR = ""
                if "ExtremeFear" in resultDICT.keys() and resultDICT["ExtremeFear"] != []:
                    responseLIST = [int(i) for i in resultDICT["ExtremeFear"]]
                    indexSTR = "ExtremeFear"
                elif "ExtremeGreed" in resultDICT.keys() and resultDICT["ExtremeGreed"] != []:
                    responseLIST = [int(i) for i in resultDICT["ExtremeGreed"]]
                    indexSTR = "ExtremeGreed"
                elif "Neutral" in resultDICT.keys() and resultDICT["Neutral"] != []:
                    responseLIST = [int(i) for i in resultDICT["Neutral"]]
                    indexSTR = "Neutral"
                elif "Fear" in resultDICT.keys() and resultDICT["Fear"] != []:
                    responseLIST = [int(i) for i in resultDICT["Fear"]]
                    indexSTR = "Fear"
                elif "Greed" in resultDICT.keys() and resultDICT["Greed"] != []:
                    responseLIST = [int(i) for i in resultDICT["Greed"]]
                    indexSTR = "Greed"
                if "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！" in responseLIST:
                    responseSTR = responseLIST[0]
                else:
                    responseSTR = "判斷結果為{}指數為{}".format(indexSTR,sum(responseLIST))
                await message.reply(responseSTR)

if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])
