#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging #可以測試哪裡有問題
import discord
import json
import re
from covid_info_bot import LokiResult, runLoki
import datetime

import vaccine_stock_api
from pprint import pprint


logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

# sideEffectTemplate ={
#                 "vaccine_shot":"",
#                  "side_effect": "",
#                  "side_effect_var":""
#                  }
# severeSideEffectTemplate = {
#     "vaccine_shot" : "",
#     "severe_side_effect" : ""
# }

# vaccineStockTemplate = {
#                 "vaccine_shot":"",
#                 "location":"",
#                 "vaccine_stock":""
#                 }

# 將全部意圖合為一個Template處理，
# 但不一定要每個intent都必須滿足才能結束對話，
# 而是當confirm = True時，就可以結束對話
allTemplate = {
    "inquiry_type" : [],
    "vaccine_shot" : [],
    "side_effect": [],
    "severe_side_effect" : [],
    "location" : [],
    "vaccine_stock" : [],
    "group_num" : [],
    "group_num_def" : [],
    "response": "",
    "followup": [],
    "updatetime": datetime.datetime.now(), #新增datetime
    "completed" : False
}

mscDICT = {
    # "userID": {side_effectTemplate, vaccine_stockTemplate, severeSideEffectTemplate}
}
# </取得多輪對話資訊>

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))


def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT, 


@client.event #成功連線到discord的回答
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    # if message.channel.name != "dt_intern":
    #     return

    if not re.search("<@[!&]{}> ?".format(message.author.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return
# try:
    print("message.author.id =", message.author.id, "\nmessage.content =", message.content)
    msgSTR = re.sub("<@[!&]{}> ?".format(message.author.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
        replySTR = "Hi 您好，想知道哪些疫苗資訊呢?"
        await message.reply(replySTR)
        return

    lokiResultDICT = getLokiResult(msgSTR)    # 取得 Loki 回傳結果
    logging.info(lokiResultDICT)  

    if lokiResultDICT:
        print(lokiResultDICT)
        if message.author.id not in mscDICT: # 判斷 User 是否為第一輪對話
            # mscDICT[message.author.id] = {
            #         "inquiry_type" : "",
            #         "vaccine_shot" : "",
            #         "side_effect": "",
            #         "severe_side_effect" : "",
            #         "location" : "",
            #         "vaccine_stock" : "",
            #         "group_num" : "", 
            #         "group_def" : "",
            #         "response": "",
            #         "followup": [],
            #         "completed" : False
            #                         }
            mscDICT[message.author.id] = allTemplate
            for k in lokiResultDICT.keys(): #注意!
                mscDICT[message.author.id][k] = lokiResultDICT[k]
            mscDICT[message.author.id]["followup"] = {}
        else:
            datetimeNow = datetime.datetime.now()
            timeDIFF = datetimeNow - mscDICT[message.author.id]["updatetime"]
            for k in lokiResultDICT.keys(): #注意!
                mscDICT[message.author.id][k] = lokiResultDICT[k]
            if timeDIFF.total_seconds() >= 300: # 回答時間超過五分鐘，對話內容重置
                # mscDICT[message.author.id]= {
                #     "inquiry_type" : "",
                #     "vaccine_shot" : "",
                #     "side_effect": "",
                #     "severe_side_effect" : "",
                #     "location" : "",
                #     "vaccine_stock" : "",
                #     "group_num" : "", #未處理
                #     "group_def" : "", #未處理           
                #     "response": "",
                #     "followup": [],
                #     "completed" : False
                #                     }
                mscDICT[message.author.id] = allTemplate
                for k in lokiResultDICT.keys(): #注意!
                    mscDICT[message.author.id][k] = lokiResultDICT[k]
                mscDICT[message.author.id]["followup"] = {}
    
    # if confirm == False : 確認不完整資訊
    # elif confirm == True : 問還要不要繼續問資訊
    if lokiResultDICT:
        # if mscDICT[message.author.id]["inquiry_type"] == "" and replySTR == "":    
        #     replySTR = "\n請問要問關於疫苗的甚麼資訊呢？"
        if mscDICT[message.author.id]["completed"] == False:
            if mscDICT[message.author.id]["followup"] != []:
                followupDICT = runLoki(mscDICT[message.author.id]["followup"], ["Probe", "confirm_check"])
                for k in followupDICT.keys():
                    mscDICT[message.author.id][k] = followupDICT[k]
                mscDICT[message.author.id]["followup"] = []
            if mscDICT[message.author.id]["response"]:
                replySTR = mscDICT[message.author.id]["response"]

            if mscDICT[message.author.id]["inquiry_type"] == [] and replySTR == "":
                replySTR = "\n請問要問關於疫苗的甚麼資訊呢？"
            
            elif mscDICT[message.author.id]["inquiry_type"] == [] and mscDICT[message.author.id]["vaccine_shot"] != [] and replySTR == "":
                replySTR = "你想知道關於這支疫苗的甚麼事情?"

            if mscDICT[message.author.id]["inquiry_type"] == "side_effect" and mscDICT[message.author.id]["vaccine_shot"] == []:
                replySTR = "你想要詢問哪隻疫苗的副作用?"
            
            if mscDICT[message.author.id]["inquiry_type"] == "severe_side_effect" and mscDICT[message.author.id]["vaccine_shot"] == []: 
                replySTR = "你想要詢問哪隻疫苗的嚴重副作用?"
            
            if mscDICT[message.author.id]["inquiry_type"] == "vaccine_stock" and mscDICT[message.author.id]["location"] == []:
                replySTR = "請問您要詢問哪個地區的疫苗庫存呢?"
            
            if mscDICT[message.author.id]["inquiry_type"] == "vaccine_stock" and mscDICT[message.author.id]["vaccine_shot"] == []:
                replySTR = "請問您想知道哪個廠牌的疫苗庫存呢?"            
            
            if mscDICT[message.author.id]["inquiry_type"] == "vaccine_stock" and mscDICT[message.author.id]["location"] == [] and mscDICT[message.author.id]["vaccine_shot"] == []:
                replySTR = "請問您想知道哪個廠牌以及哪個地區的疫苗庫存呢?"  

            if mscDICT[message.author.id]["inquirt_type"] == "group" and replySTR == "":
                replySTR += """{}族群為{}。\n""".format("".join(mscDICT[message.author.id]["group_num"]), "".join(mscDICT[message.author.id]["group_num_def"]))
                await message.reply(replySTR)
                replySTR = "還想問其他的嗎?" 
                del mscDICT[message.author.id]

            if "side_effect" in mscDICT[message.author.id]["inquiry_type"] and mscDICT[message.author.id]["vaccine_shot"] != []:
                replySTR += """{}疫苗的常見副作用是{}。\n""".format("".join(mscDICT[message.author.id]["vaccine_shot"]), "".join(mscDICT[message.author.id]["side_effect"]))
                await message.reply(replySTR)
                replySTR = "還想問其他的嗎?" 
                del mscDICT[message.author.id]

            if "severe_side_effect" in mscDICT[message.author.id]["inquiry_type"] and mscDICT[message.author.id]["vaccine_shot"] != []:
                replySTR += """{}疫苗的常見副作用是{}。\n""".format("".join(mscDICT[message.author.id]["vaccine_shot"]), "".join(mscDICT[message.author.id]["severe_side_effect"]))
                await message.reply(replySTR)
                replySTR = "還想問其他的嗎?"
                del mscDICT[message.author.id]

            if "vaccine_stock" in mscDICT[message.author.id]["inquiry_type"] and mscDICT[message.author.id]["location"] != [] and mscDICT[message.author.id]["vaccine_shot"] != []:
                replySTR = vaccine_stock_api.write_response(mscDICT[message.author.id])
                await message.reply(replySTR)
                replySTR = "還想問其他的嗎?"
                del mscDICT[message.author.id]

            if replySTR == "":
                print("看到我就是種錯誤囉!")
        else:  
            del mscDICT[message.author.id]
            replySTR = "對話結束囉! 謝謝你使用Covid_Info_Bot! 請務必給我們五個星喔XDD"

    print("mscDICT =")
    pprint(mscDICT)

    if replySTR:    # 回應 User 訊息
        await message.reply(replySTR)
    return

#except Exception as e:
    # logging.error("[MSG ERROR] {}".format(str(e)))
    # print("[MSG ERROR] {}".format(str(e)))


if __name__ == "__main__":
    client.run(accountDICT["discord_token"])