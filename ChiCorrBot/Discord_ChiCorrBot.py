#!/user/bin/env python
# -*- coding: utf-8 -*-

import discord
import json
import logging
import re
from ArticutAPI import Articut
from ChiCorrBot import runLoki, explanationDICT
from datetime import datetime
from pprint import pprint
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi
from pypinyin import lazy_pinyin, Style  
from typing import Counter
from unicodedata import name
from unittest import result
from urllib import response

hmmparams = DefaultHmmParams()
style = Style.TONE3

logging.basicConfig(level=logging.DEBUG)


with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR, filterLIST=[]):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    #filterLIST = []
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
        #templateDICT["counter"] = 0 #新增counter
        return templateDICT

    async def on_ready(self):
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "name":"",
                             "time":"",

        }
        self.mscDICT = { #userid:templateDICT
        }
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None
        elif message.content.lower().replace(" ", "") in ("bot點名",):
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
                    replySTR = f'{msgSTR.title()}，你的華語名字是什麼呀？'
                    self.mscDICT[message.author.id]["latestQuest"] = replySTR
                    #設定每次counter都加一
                    #self.mscDICT[message.author.id]['counter'] += 1

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話

                #確認是否繼續檢查華語病句
                if msgSTR.lower() in 'bye,bye bye,byebye,good bye,拜拜,拜咿,掰掰'.split(','):
                    #刪除之前的對話，並給予結束的回覆。
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = '拜拜，我們下次見囉！'

                #從這裡開始接上 NLU 模型
                #設定counter的次數，判斷intent。
                else:
                    #第一次處理：姓名，使用intnet:name
                    if self.mscDICT[message.authhor.id]["name"] == "":
                    #if self.mscDICT[message.author.id]['counter'] == 1:
                        resultDICT = getLokiResult(msgSTR, ['name'])
                        logging.debug("######\nLoki 處理結果如下：")
                        logging.debug(resultDICT)
                        replySTR = resultDICT['greeting']
                        #self.mscDICT[message.author.id]['counter'] += 1
                    #第二次處理：時間，使用intent:time
                    elif self.mscDICT[message.authhor.id]["time"] == "":
                    #elif self.mscDICT[message.author.id]['counter'] == 2:
                        resultDICT = getLokiResult(msgSTR, ['time'])
                        logging.debug("######\nLoki 處理結果如下：")
                        logging.debug(resultDICT)
                        replySTR = resultDICT['time']
                        #self.mscDICT[message.author.id]['counter'] += 1
                    #第三次處理：病句，使用intent:syntax,semantics,vocabulary,ans
                    else:
                        resultDICT = getLokiResult(msgSTR, ['syntax', 'semantics', 'vocabulary','ans'])
                        logging.debug("######\nLoki 處理結果如下：")
                        logging.debug(resultDICT)
                        #如果resultDICT是空字典
                        if not resultDICT: 
                            replySTR = '本bot覺得你的句子是對的！'
                        #如果resultDICT不是空字典
                        else:
                            #inq有兩種可能，一是確認語意問題，二是使用者的回覆是或否。
                            self.mscDICT[message.author.id]['inq'] = resultDICT['inq']
                            if 'suggestion' in resultDICT:
                                self.mscDICT[message.author.id]['suggestion'] = resultDICT['suggestion']
                            if 'error' in resultDICT:
                                self.mscDICT[message.author.id]['error'] = resultDICT['error']

                            ChiSuggest = self.mscDICT[message.author.id]['suggestion']
                            PinyinSuggest = ' '.join(lazy_pinyin(ChiSuggest,style=style))

                            res = f"那你可以說：\n「{ChiSuggest}」\n「{PinyinSuggest}」"
                            expl = f"\n錯誤說明：{explanationDICT[self.mscDICT[message.author.id]['error']]}"
                            req = '\n你還有其他句子要討論嗎？如果有，請繼續輸入句子，如果沒有，請輸入「Bye」。'
                            replySTR = f'{res}\n{expl}\n{req}'

                            #不需要再次詢問的intent(syntax,vocabulary)，則直接印出建議句子和錯誤說明。
                            if not self.mscDICT[message.author.id]['inq']:
                                replySTR = replySTR
                            #辨識回答為「是」，則印出建議句子和錯誤說明。
                            elif self.mscDICT[message.author.id]['inq'] == '是':
                                replySTR = replySTR
                            #辨識回答為「否」，則印出該回答。
                            elif self.mscDICT[message.author.id]['inq'] == '否':
                                replySTR = f'啊！本bot不知道，只好請教老師了!\n{req}'
                            #需要再次確認語意的intent(semantics)，則印出該問題。
                            else:
                                replySTR = self.mscDICT[message.author.id]['inq']

                    
                
        await message.reply(replySTR)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])