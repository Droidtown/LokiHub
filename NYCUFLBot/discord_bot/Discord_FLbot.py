#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

from datetime import datetime
from pprint import pprint
from requests import post
from time import sleep

from copytoaster_api import getCopyToasterResult
hashtagLIST = ["傳技", "高寫", "英作", "英文作文", "第二外語", "加退選", "同一語種", "專業必選",
               "114學年度前", "114學年度後", "系排名", "相關組別", "推薦信", "推薦函", "預修生",
               "應修", "應選", "預修", "指導教授", "同意書", "學士學位", "研究生", "抵免",
               "校園單一入口", "陽明交大外文系", "教務處", "課務組", "跨學域", "漢語語言學", "AI",
               "人工智能", "人工智慧", "認知科學", "程式設計", "本體知識", "語言學", "學程",
               "外文系", "外文所", "人學中心", "語意學", "程式設計", "程設", "Python", "必修課程",
               "計算機概論", "計概", "必修課程", "交換留學", "交換生", "所務會議", "系務會議", "成績",
               "外所老師", "原創性", "共同指導同意書", "資格考", "更換指導", "A制", "B制", "論文計劃書",
               "計劃書", "A 制", "B 制", "論文計畫書", "計畫書"]

logging.basicConfig(level=logging.DEBUG)

def composeAnsWithLLM(assistant, inputSTR):
    url = "https://api.droidtown.co/Loki/Call/" # 中文版
    payload = {
      "username": accountDICT["username"],
      "func": "call_llm",
      "data": {
        "model": "Gemma2-9B", # [Gemma2-9B, Gemma3-12B, Gemma3-27B, Llama3-8B, Llama3-70B, Llama3-Taiwan-8B, Llama3.3-70B, Phi3-3B, Phi4-14B, Nemotron-4B]
        "system": "你是大學裡的系辦公室助理 Chatbot. 你會嚴格參考以下的資料回答學生的問題。", # optional
        "assistant": assistant, # optional
        "user": f"依前述參考文件，回答學生提問的 {inputSTR}", # required
      }
    }

    result = post(url, json=payload).json()
    return result


def getLokiTextSim(inputSTR, keywordLIST=[], featureLIST=[], count=1):
    payloadDICT = {
        "username": accountDICT["username"],
        "loki_key": accountDICT["loki_key"],
        "input_str": inputSTR,
        "keyword": keywordLIST,
        "feature": featureLIST,
        "count": count
    }
    LOKI_URL = "https://api.droidtown.co/Loki/API/"
    POST_INTERVAL_SEC = 5

    while True:
        response = post(LOKI_URL, json=payloadDICT)
        if response.status_code == 200:
            try:
                resultDICT = response.json()
                if resultDICT["status"]:
                    if resultDICT["progress_status"] == "processing":
                        sleep(POST_INTERVAL_SEC)
                        continue
                return resultDICT
            except Exception as e:
                return {"status": False, "msg": str(e)}
        else:
            return {"status": False, "msg": "HTTP {}".format(response.status_code)}


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
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('{} 上線囉！耶≡'.format(self.user, self.user.id))

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

                """
                bot 處理過程參考 (以下項目根據專案可互相配合或調換順序)
                ● Loki 語意分析 (askLoki)，結果最為嚴謹，可視為第一處理項目
                ● Similarity 相似度比對 (simLoki)，計算 Loki 模型中的訓練句型相似度，門檻值為 account.info 中的 utterance_threshold
                ● ContentWord 脈絡模糊比對 (ARTICUT.getContentWordLIST)，將脈絡作為關鍵字查詢出相關的資料
                ● LLM 生成模型 (askLLM)，除了 msgSTR 外，建議將相關的資料一併附上，以獲得更精確的結果
                """
                # Loki 語意分析

                #<1> 先讓 Loki 確認這個問題和哪些領域分類有關，並存入 categoryLIST 內。
                resultDICT = getLokiTextSim(inputSTR=msgSTR, keywordLIST=hashtagLIST, featureLIST=["noun", "verb", "modifier"])
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                replySTR = ""
                categoryLIST = []
                if resultDICT["status"] == True:
                    categoryLIST.append(resultDICT["results"][0]["syntax"])
                    categoryLIST.append(resultDICT["results"][0]["lexicon"])
                else:
                    pass

                #<2> 把每個領域分類搭配使用者的提問，查詢 copytoaster 裡是否有相關參考文件。
                assistantLIST = []
                userSTR = msgSTR
                for c in categoryLIST:
                    copytoasterResultDICT =  getCopyToasterResult(c, msgSTR, count=1)
                    logging.debug("copytoaster 的搜尋結果：", copytoasterResultDICT)
                    if copytoasterResultDICT["status"] == False:
                        pass
                    else:
                        assistantLIST.append(copytoasterResultDICT["result_list"][0]["document"])

                if assistantLIST != []:
                    assistantSTR = "\n".join(assistantLIST)
                    #<3> 把使用者的提問，以及參考文件一起傳給 LLM，讓它組裝成一則自然通順的回覆文字
                    replyDICT = composeAnsWithLLM(assistant=assistantSTR, inputSTR=userSTR)
                    if replyDICT["status"] == True:
                        replySTR = replyDICT["result"][0]["message"]["content"]
                else:
                    #<4> 救濟方案！如果無法回答的話…
                    if replySTR == "":
                        replySTR = "抱歉，今天系辦秘書 Chatbot 休假沒來，我只是代班收信的 Chatbot. 同學你自己上系所網頁查詢，或是明天再來問好嗎？"
            await message.reply(replySTR)


if __name__ == "__main__":

    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
