#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint
# from home_run_taipei.main import askLoki
from RSBot.main import askLoki, askLLM, getSimilarity, simLoki, ARTICUT
from Get_reply import reply_maker


logging.basicConfig(level=logging.DEBUG)

def getLokiResult(inputSTR, filterLIST=[]):
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"] #
    # 設定參考資料
    refDICT = { # value 必須為 list
        #"key": []
        "items" : [], 
        "brand" : [], 
        "goal": []
        
    }
    resultDICT = askLoki(inputSTR, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
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
                             "false_count" : 0,
                             "items" : [], 
                             "brand" : [], 
                             "goal": [],
                             "response": []

        }
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
        print(f"message {message}")
        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
  
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "":
                msgSTR == "hi"
           
                
# ##########初次對話：這裡是 keyword trigger 的。
            if msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)

                        # replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                        replySTR = "long time no see. What do you want to find"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    # replySTR = msgSTR.title()
                    replySTR = "hello! I am a recommend bot. I am selling electronics. You can tell me what you want to find."
            elif message.author.id not in self.mscDICT.keys():
                self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                self.refDICT = { # value 必須為 list
                            #"key": []
                            "items" : [], 
                            "brand" : [], 
                            "goal": [],
                            "response": []
                            
                            } 
                replySTR = "hello! I am a recommend bot. I am selling electronics. You can tell me what you want to find."   
# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型

                """
                bot 處理過程參考 (以下項目根據專案可互相配合或調換順序)
                ● Loki 語意分析 (askLoki)，結果最為嚴謹，可視為第一處理項目
                ● Similarity 相似度比對 (simLoki)，計算 Loki 模型中的訓練句型相似度，門檻值為 account.info 中的 utterance_threshold
                ● ContentWord 脈絡模糊比對 (ARTICUT.getContentWordLIST)，將脈絡作為關鍵字查詢出相關的資料
                ● LLM 生成模型 (askLLM)，除了 msgSTR 外，建議將相關的資料一併附上，以獲得更精確的結果
                """
                # Loki 語意分析
                #askLoki(content, **kwargs)
                # for key_ in self.refDICT:
                #     self.refDICT[key_] = self.mscDICT[message.author.id][key_].copy()
                refDICT = {
                "items": self.mscDICT[message.author.id]["items"][:],
                "brand": self.mscDICT[message.author.id]["brand"][:],
                "goal": self.mscDICT[message.author.id]["goal"][:],
                "response": self.mscDICT[message.author.id]["response"][:],
            }
                resultDICT = askLoki(msgSTR, refDICT=refDICT)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                if len(resultDICT["response"]) > 0:
                    replySTR = resultDICT["response"][0]
                else:
                    resultDICT2  = simLoki(msgSTR)
                    simUtter = [i for i in resultDICT2.keys()]
                    if simUtter != []:
                        resultDICT3 = askLoki(resultDICT2[simUtter[0]][msgSTR]["utterance"], refDICT={"reply":[]})
                        
                        if len(resultDICT3["response"]) > 0:
                            replySTR = resultDICT3["response"][0]
                        else:
                            replySTR = "no items"
                    else:
                        replySTR = "I don't understand what you mean"
                # final_resultDICT = resultDICT
                # replySTR = reply_maker(final_resultDICT)
                # if resultDICT['source'] == ['LLM_reply']:
                #     resultDICT2  = simLoki(msgSTR)
                #     simUtter = [i for i in resultDICT2.keys()]
                #     if simUtter != []:
                #         resultDICT3 = askLoki(resultDICT2[simUtter[0]][msgSTR]["utterance"], refDICT={"reply":[]})
                #         final_resultDICT = resultDICT3
                #         replySTR = resultDICT3['reply'][0]
                #     else:
                #         replySTR = resultDICT["response"]
                
                # replySTR = "抱歉，我的資料庫裡沒有相關的知識！"  # 預設回覆
                # if resultDICT["response"] != [] and resultDICT["source"] != ["LLM_reply"]:
                #     replySTR = resultDICT["response"][0]
                # else:
                #     """
                #     # Similarity 相似度比對
                #     simDICT = simLoki(msgSTR)
                #     # ContentWord 脈絡模糊比對
                #     atkDICT = ARTICUT.parse(msgSTR)
                #     contentWordLIST = ARTICUT.getContentWordLIST(atkDICT)
                #     # LLM 生成模型
                #     responseSTR = askLLM(system, assistant, user)
                #     """
                #     assistantSTR = "！"
                #     userSTR = msgSTR
                #     #askLLM(system="", assistant="", user="")
                #     replySTR = askLLM(assistant=assistantSTR, user=userSTR)

                # for key_ in self.refDICT:
                #     self.mscDICT[message.author.id][key_] = self.refDICT[key_].copy()
                # ★ 把 refDICT 寫回使用者短期記憶（保持狀態延續）
                self.mscDICT[message.author.id]["items"] = resultDICT["items"][:]
                self.mscDICT[message.author.id]["brand"] = resultDICT["brand"][:]
                self.mscDICT[message.author.id]["goal"] = resultDICT["goal"][:]
            self.mscDICT[message.author.id]["latestQuest"] = msgSTR
            self.mscDICT[message.author.id]["updatetime"] = datetime.now()        
            print(self.mscDICT)
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("./RSBot/account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
