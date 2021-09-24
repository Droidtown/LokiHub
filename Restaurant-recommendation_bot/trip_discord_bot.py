#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import datetime

from RestaurantAndHotel_bot import runLoki
from pprint import pprint


logging.basicConfig(level=logging.CRITICAL)

# <取得多輪對話資訊>
client = discord.Client()

#
# command_templateDICT = {"city": None,
#                 "area": None,
#                 "shop": {},
#                 "updatetime": datetime.datetime.now(),
#                 "completed": False
#                 }
#
# reservation_templateDICT = {"people": None,
#                 "time": None,
#                 "restaurant_name": {}, #2個值:餐廳name, 能否預約
#                 "updatetime": datetime.datetime.now(),
#                 "completed": False
#                 }

new_templateDICT = {"city": None,
                    "area": None,
                    "restaurant_name": {}, #2個值:餐廳name, 能否預約
                    "people": None,
                    "time": None,
                    "updatetime": datetime.datetime.now(),
                    "completed": False
                    }


mscDICT = {
    # "userID": {new_templateDICT}
}
# </取得多輪對話資訊>

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))

with open(r"./data/restaurant_domain.json", encoding="UTF-8") as f:
    restaurantDICT = json.load(f)

#增加函式:將json檔內的所有餐廳集中為List
def get_restaurantLIST(jsonfile):
    res_LIST = []
    for city in jsonfile.keys():
        for area in jsonfile[city].keys():
            for name in jsonfile[city][area].keys():
                res_LIST.append(name)
    return res_LIST

#增加函式:取得該餐廳是否能預約
def get_reservation(jsonfile, msgSTR):
    for city in jsonfile.keys():
        for area in jsonfile[city].keys():
            for name in jsonfile[city][area]:
                if name == msgSTR:
                    return (jsonfile[city][area][msgSTR]["預約"])

#增加函式:取得該餐廳的評價
def get_evaluation(jsonfile, msgSTR):
    for city in jsonfile.keys():
        for area in jsonfile[city].keys():
            for name in jsonfile[city][area]:
                if name == msgSTR:
                    return (jsonfile[city][area][msgSTR]["評價"])

#增加函式:取得該餐廳的地址
def get_location(jsonfile, msgSTR):
    for city in jsonfile.keys():
        for area in jsonfile[city].keys():
            for name in jsonfile[city][area]:
                if name == msgSTR:
                    return (jsonfile[city][area][msgSTR]["地址"])

#增加函式:取得該餐廳的價位
def get_perchase(jsonfile, msgSTR):
    for city in jsonfile.keys():
        for area in jsonfile[city].keys():
            for name in jsonfile[city][area]:
                if name == msgSTR:
                    return (jsonfile[city][area][msgSTR]["價位"])

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT



@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    # if message.channel.name != "bot_test":  這是為了測試用的，不註解掉會無法紀錄及回覆訊息
    #     return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return


    print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
    msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    RestaurantLIST = get_restaurantLIST(restaurantDICT)   # 這邊透過get_restaurantLIST函式得到包含所有餐廳的list
    lokiResultDICT = getLokiResult(msgSTR)  # 取得 Loki 回傳結果
    if re.search("(hi|hello|哈囉|嗨|[你您]好)", msgSTR.lower()):
        replySTR = "Hi 您好，這邊可以推薦您所在地區的餐廳及美食，可以先告訴我你在哪個縣市喔"
        await message.reply(replySTR)
        return

    # elif re.search("(這附近有什麼(好|可以?)吃的|我想吃(東西|[晚午早]餐))", msgSTR):  #測試用
    #     replySTR = "請問您在哪個縣市呢?"
    #     await message.reply(replySTR)
    #     return

    elif re.search("(沒有問題(了?)|ok|這樣就(行|可以|ok|沒問題)了|沒問題)", msgSTR.lower()):
        mscDICT[message.author]["completed"] = True
        print("mscDICT =", end=" ")
        pprint(mscDICT)

        if mscDICT[message.author]["completed"] == True: # 清空 User Dict
            del mscDICT[message.author]

        replySTR = "好的感謝您的使用祝用餐愉快"
        await message.reply(replySTR)
        return

    if lokiResultDICT:
        if message.author not in mscDICT:    # 判斷 User 是否為第一輪對話
            mscDICT[message.author] = {"city": "",
                                       "area": "",
                                       "restaurant_name": {}, #2個值:餐廳name, 能否預約
                                       "people": None,
                                       "time": None,
                                       "updatetime": datetime.datetime.now(),
                                       "completed": False
                                       }
        else:
            datetimeNow = datetime.datetime.now()  # 取得當下時間
            timeDIFF = datetimeNow - mscDICT[message.author]["updatetime"]
            if timeDIFF.total_seconds() <= 300:  # 以秒為單位，5分鐘以內都算是舊對話
                mscDICT[message.author]["updatetime"] = datetimeNow

        for k in lokiResultDICT.keys():
            if k == "city":
                mscDICT[message.author]["city"] = lokiResultDICT["city"]


            elif k == "area":
                mscDICT[message.author]["area"] = lokiResultDICT["area"]


            elif k == "res_person":
                mscDICT[message.author]["people"] = lokiResultDICT["res_person"][0]


            elif k == "res_time":
                mscDICT[message.author]["time"] = lokiResultDICT["res_time"]

            elif k == "reserve":
                if mscDICT[message.author]["restaurant_name"]["預約"] == "yes":
                    replySTR = "好的,請問幾位?"
                else:
                    replySTR = "不好意思，該店家不提供預約服務，請以現場情狀為準。"
                    mscDICT[message.author]["restaurant_name"] = {}

            elif k == "res_loc":
                replySTR = "這家店的位置在:\n{}".format(get_location(restaurantDICT, msgSTR=mscDICT[message.author]["restaurant_name"]["name"]))

            elif k == "res_eva":
                replySTR = "這家店的評價為:\n\n{}\n\n以上資訊為參考每人主觀不同還請以實際情形為準".format(get_evaluation(restaurantDICT, msgSTR=mscDICT[message.author]["restaurant_name"]["name"]))

            elif k == "res_price":
                replySTR = "這家店的價位為:\n<{}>".format(get_perchase(restaurantDICT, msgSTR=mscDICT[message.author]["restaurant_name"]["name"]))


        if mscDICT[message.author]["city"] == "" and replySTR == "":
            replySTR = "請問你在哪個縣市呢?"

        elif mscDICT[message.author]["area"] == "" and replySTR == "":
            replySTR = "請問您在哪個地區呢?"

        elif mscDICT[message.author]["city"] == "Nothing" and replySTR == "":
            replySTR = "不好意思，您所輸入的縣市可能還未加入資料庫中，還請輸入其他縣市或是等候下次更新的加入"


        elif mscDICT[message.author]["city"] != "Nothing" and mscDICT[message.author]["area"] != "Nothing" and mscDICT[message.author]["people"] == None and mscDICT[message.author]["time"] == None and replySTR == "":
            # print(restaurantDICT[mscDICT[message.author]["city"]][mscDICT[message.author]["area"]])
            replySTR = """以下推薦{}家餐廳給您，分別為:\n{}。\n請問有您喜歡的店家嗎?""".format(len(restaurantDICT[mscDICT[message.author]["city"]][mscDICT[message.author]["area"]].keys()),
                                                                       ", ".join(i for i in restaurantDICT[mscDICT[message.author]["city"]][mscDICT[message.author]["area"]].keys()))

        # ###9/18增加
        elif mscDICT[message.author]["people"] != None and mscDICT[message.author]["time"] == None and replySTR == "":
            replySTR = "好的人數為{}位,請問大約幾點到呢?".format(mscDICT[message.author]["people"])

        elif mscDICT[message.author]["time"] != None and replySTR == "":
            replySTR="""好的這邊跟您確認預約資訊為: \n預約人數:{}位\n預約時間:{}\n預約餐廳:{}\n請問以上資訊有誤嗎?""".format(mscDICT[message.author]["people"], mscDICT[message.author]["time"], mscDICT[message.author]["restaurant_name"]["name"])
        # ###9/18增加
    elif msgSTR in RestaurantLIST:
        replySTR = "好的您選擇的店家是:{}，請問還需要其他服務嗎?".format(msgSTR)
        mscDICT[message.author]["restaurant_name"]["name"] = msgSTR
        if get_reservation(jsonfile=restaurantDICT, msgSTR=msgSTR) == "是":  # 判斷該餐廳是否能預約
            mscDICT[message.author]["restaurant_name"]["預約"] = "yes"
        else:
            mscDICT[message.author]["restaurant_name"]["預約"] = "no"


    # mscDICT[message.author]["completed"] = True
    print("mscDICT =", end=" ")
    pprint(mscDICT)

    # if mscDICT[message.author]["completed"] == "True":    # 清空 User Dict
    #     del mscDICT[message.author]

    if replySTR:    # 回應 User 訊息
        await message.reply(replySTR)
    return




if __name__ == "__main__":
    client.run(accountDICT["discord_token"])
    # getLokiResult("這附近有什麼吃的，我在台南市，在中西區")