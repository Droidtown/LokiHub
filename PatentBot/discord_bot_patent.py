#!/user/bin/env python
# -*- coding: utf-8 -*-


import logging
import discord
import json
import re
import datetime

from PatentBot import runLoki
from Patent_Articut import articut4PatentBot
from pprint import pprint


logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

patentTemplate = {"IPC_Number":"",
                  "Type":"",
                  "Content":"",
                  "ArticutresultDICT":"",
                  "updatetime":datetime.datetime.now(),
                  "completed":""}

mscDICT = {}
# </取得多輪對話資訊>

codeDICT = {"_M": "新型", "_I": "發明", "_D": "設計"} # 可另外新建一個dict再import


with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

# 接上NLU模型: PatentBot
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

# 接上Articut分析模型: articut4PatentBot
def getArticutResult(IPC_Number, Type, inputSTR):
    categoryFILE = IPC_Number + Type
    resultDICT = articut4PatentBot(categoryFILE, inputSTR)
    print("Articut Result => {}".format(resultDICT))
    return resultDICT



@client.event
async def on_ready():
    #logging.info("[READY INFO] {} 上工啦!".format(client.user))
    print("[READY INFO] {} 上工啦!".format(client.user))


@client.event
async def on_message(message):
    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return

    print("收到來自 {} 的訊息".format(message.author), "\n訊息內容是 {}: ".format(message.content))
    msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    msgSTR = re.sub("[喔啊耶呢滴啦齁的]", "。", msgSTR)  # 將語尾助詞取代成"。"
    print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
        replySTR = "Hi，您想比對哪個領域的專利呢？"
        await message.reply(replySTR)
        return

    if len(msgSTR) < 24:
        lokiResultDICT = getLokiResult(msgSTR) # 取得 Loki 回傳結果

        if lokiResultDICT:
            if message.author.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[message.author.id] = {"completed":False,
                                              "updatetime":datetime.datetime.now()}
            else:
                datetimeNow = datetime.datetime.now() # 取得當下時間
                timeDIFF = datetimeNow - mscDICT[message.author.id]["updatetime"]
                if timeDIFF.total_seconds() <= 300: # 以秒為單位，5分鐘內都算是舊對話
                    mscDICT[message.author.id]["updatetime"] = datetimeNow

            for k in lokiResultDICT:    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if "IPC_Number" in lokiResultDICT.keys() and k == "IPC_Number":
                    mscDICT[message.author.id]["IPC_Number"] = lokiResultDICT["IPC_Number"]
                if "Type" in lokiResultDICT.keys() and k == "Type":
                    mscDICT[message.author.id]["Type"] = lokiResultDICT["Type"]
                if "msg" in lokiResultDICT.keys() and k == "msg" and (("IPC_Number" not in mscDICT[message.author.id].keys()) or ("Type" not in mscDICT[message.author.id].keys())):
                    replySTR = lokiResultDICT[k]
                    print("Loki msg:", replySTR, "\n")
                    await message.reply(replySTR)
                    return
                
                if "confirm" in lokiResultDICT and k == "confirm":
                    if lokiResultDICT["confirm"]:
                        replySTR = "正在為您比對的是IPC_Number為{}中類型為{}的專利，請您稍後片刻，謝謝...".format(mscDICT[message.author.id]["IPC_Number"], codeDICT[mscDICT[message.author.id]["Type"]]).replace("    ", "")
                        await message.reply(replySTR)
                        # 確認後將文本送入Articut分析
                        ArticutresultDICT = getArticutResult(mscDICT[message.author.id]["IPC_Number"], mscDICT[message.author.id]["Type"], mscDICT[message.author.id]["Content"])
                        mscDICT[message.author.id]["ArticutresultDICT"] = ArticutresultDICT
                        # 檢查是否已經完成對話
                        if set(patentTemplate.keys()).difference(mscDICT[message.author.id].keys()) == set():
                            url = "https://twpat4.tipo.gov.tw/tipotwoc/tipotwkm?!!FR_" + list(mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"].keys())[0]
                            replySTR = """為您找到最相似的專利為證書號 {} 的專利，
                            其"{}"的餘弦相似度經過Articut的分析為 {:.2f} ，
                            更完整的專利文件請參考: {}""".format(list(mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"].keys())[0],
                                                               mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"].keys())[0]][1],
                                                               mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"][list(mscDICT[message.author.id]["ArticutresultDICT"]["All_Max"].keys())[0]][0],
                                                               url).replace("    ", "")
                            await message.reply(replySTR)
                            mscDICT[message.author.id]["completed"] = True
                            print("mscDICT = ")
                            pprint(mscDICT)
                            if mscDICT[message.author.id]["completed"]:    # 清空 User Dict
                                del mscDICT[message.author.id]
                        return

                    else:
                        replySTR = "請重新輸入您想比對哪個領域的專利範圍..."
                        await message.reply(replySTR)
                        return

            if mscDICT[message.author.id]["IPC_Number"] != "" and mscDICT[message.author.id]["Type"] != "":
                replySTR = "請輸入您想比對的專利範圍..."
                print("Loki msg:", replySTR, "\n")
                await message.reply(replySTR)
                return
            
        else:
            replySTR = "您輸入的領域或類型似乎是錯誤的，請重新輸入..."
            await message.reply(replySTR)
            return

    else:
        mscDICT[message.author.id]["Content"] = msgSTR
        replySTR = "再次確認您想比對的是IPC_Number為{}中類型為{}的專利，沒錯嗎?".format(mscDICT[message.author.id]["IPC_Number"], codeDICT[mscDICT[message.author.id]["Type"]])
        await message.reply(replySTR)
        return




                
if __name__ == "__main__":
    client.run(accountDICT["discord_token"])
