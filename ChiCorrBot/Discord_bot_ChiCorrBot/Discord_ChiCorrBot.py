#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from urllib import response
from datetime import datetime
from pprint import pprint
from ChiCorrBot import runLoki, explanationDICT

logging.basicConfig(level=logging.DEBUG)


with open("account.info", encoding="utf-8") as f: #讀取account.info
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
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "你輸入一個華語句子，讓我來幫你檢查有沒有錯誤！",

        }
        self.mscDICT = { #userid:templateDICT
        }
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
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
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

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
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title()

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                if not resultDICT: #如果resultDICT為空字典
                    replySTR = '本bot覺得你的句子是對的！'
                else: #如果resultDICT不是空字典
                    self.mscDICT[message.author.id]['inq'] = resultDICT['inq']
                    if not resultDICT['suggestion']: #當使用者回覆是否時，先保留病句的建議句子和錯誤說明。
                        self.mscDICT[message.author.id]['suggestion'] = resultDICT['suggestion']
                    if not resultDICT['error']:
                        self.mscDICT[message.author.id]['error'] = resultDICT['error']

                    res = f"那你可以說：{self.mscDICT[message.author.id]['suggestion']}"
                    expl = f"錯誤說明：{explanationDICT[self.mscDICT[message.author.id]['error']]}"
                    replySTR = f'{res}\n{expl}'

                    if not self.mscDICT[message.author.id]['inq']: #不需要再次詢問的intent(vocabulary,syntax)，則直接印出建議句子和錯誤說明。
                        replySTR = replySTR
                    elif self.mscDICT[message.author.id]['inq'] == '是': #辨識回答為「是」，則印出建議句子和錯誤說明。
                        replySTR = replySTR
                    elif self.mscDICT[message.author.id]['inq'] == '否': #辨識回答為「否」，則印出該回答。
                        replySTR = '啊！本bot不知道，只好請教老師了！'
                    else:
                        replySTR = self.mscDICT[message.author.id]['inq']
              
        await message.reply(replySTR)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])