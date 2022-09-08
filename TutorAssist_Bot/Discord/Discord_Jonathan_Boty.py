#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint
from discord.ext import commands

from Tutor_Assist_Bot import runLoki

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
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                            "latestQuest": "",
                            "msgSTR":"",
                            "requiredInfo":{}
                            
               }
        self.mscDICT = { self.user.id:{"updatetime" : None,
                            "lastInfoQuest":"",
                            "latestQuest": "",
                            "savedIntent":"",
                            "msgSTR":"",
                            "requiredInfo":{}
                            
               } #userid:templateDICT
               }
               # ####################################################################################


    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        #message.reply("Bot Assistant上線囉!請@我讓我開始為您服務!")
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
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello","早安","午安","晚安","","老師好","老師您好","老師"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "您好，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = "您好，剛才正好說到一半，您剛才說: {}".format(self.mscDICT[message.author.id]["lastInfoQuest"]) 
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "您好，我是 Bot Assistant，我會在老師不在時幫忙處理課程異動事宜！"

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                self.mscDICT[message.author.id]["msgSTR"] = msgSTR
                self.mscDICT[message.author.id]["latestQuest"] = msgSTR
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                if len(resultDICT["intentLIST"]) == 1: 
                    if "day_off" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        self.mscDICT[self.user.id]["savedIntent"] = "day_off"
                        if resultDICT["day_off"]["CancelKeyword"]=="unknown":
                            replySTR= "您要請假嗎？若您想要請假，您可以說：「王小明八月八日英文課請假。」"
                        elif resultDICT["day_off"]['CancelTimeText']== "unknown":
                            if resultDICT["day_off"]["Course/Student"] == "unknown":
                                replySTR = "Bot Assistant 需要您告知要{}的日期喔！".format(resultDICT["day_off"]['CancelKeyword'])
                            else :
                                replySTR= "Bot Assistant 需要您告知{}要{}的日期喔！".format(resultDICT["day_off"]["Course/Student"],resultDICT["day_off"]['CancelKeyword'])
                        else:
                            if resultDICT["day_off"]["Course/Student"] == "unknown":
                                if resultDICT["day_off"]["CancelDate"] == "unknown":
                                    replySTR = "好的，\n{}{}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["day_off"]['CancelKeyword'],resultDICT["day_off"]['CancelTimeText'], resultDICT["day_off"]['CancelKeyword'])
                                else:    
                                    replySTR = "好的，\n{}{}。\n確切日期： {}\n麻煩您確認一下這樣對嗎？".format(resultDICT["day_off"]['CancelTimeText'], resultDICT["day_off"]['CancelKeyword'], resultDICT["day_off"]['CancelDate'])
                            else:
                                if resultDICT["day_off"]["CancelDate"] == "unknown":
                                    replySTR = "好的，\n{}{}{}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["day_off"]['Course/Student'], resultDICT["day_off"]['CancelKeyword'],resultDICT["day_off"]['CancelTimeText'])
                                else:    
                                    replySTR = "好的，\n{}{}{}。\n確切日期： {}\n麻煩您確認一下這樣對嗎？".format(resultDICT["day_off"]["CancelTimeText"],resultDICT["day_off"]['Course/Student'], resultDICT["day_off"]['CancelKeyword'], resultDICT["day_off"]['CancelDate'])
                        self.mscDICT[self.user.id]["requiredInfo"]["day_off"] = resultDICT["day_off"]
                    elif "class_arrangement" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        self.mscDICT[self.user.id]["savedIntent"]="class_arrangement"
                        if resultDICT["class_arrangement"]["Course/Student"] == "unknown" or resultDICT["class_arrangement"]["Course/Student"] == "":
                            if resultDICT["class_arrangement"]["AlterTime"] == "unknown":
                                if resultDICT["class_arrangement"]["EarlyOrLate"] == "unknown":
                                    replySTR = "課程時間需要如何調整呢？若您想要調課，您可以說：「王小明的英文課改到八月十日。」"
                                else:
                                    if resultDICT["class_arrangement"]["AlterTimeSpan"] == "unknown":
                                        replySTR="課程時間需要{}到什麼時候呢？".format(resultDICT["class_arrangement"]["EarlyOrLate"])
                                    else:
                                        replySTR="好的，\n課程時間{} {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["EarlyOrLate"],resultDICT["class_arrangement"]["AlterTimeSpan"])
                            else:
                                if resultDICT["class_arrangement"]["EarlyOrLate"] == "unknown":
                                    replySTR="好的，\n課程時間改到 {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["AlterTime"])
                                else:
                                    replySTR="好的，\n課程時間{}到 {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["EarlyOrLate"],resultDICT["class_arrangement"]["AlterTime"])
                        else:
                            if resultDICT["class_arrangement"]["AlterTime"] == "unknown":
                                if resultDICT["class_arrangement"]["EarlyOrLate"] == "unknown":
                                    replySTR = "{}的時間需要做什麼調整嗎？".format(resultDICT["class_arrangement"]["Course/Student"])
                                else:
                                    if resultDICT["class_arrangement"]["AlterTimeSpan"] == "unknown":
                                        replySTR="{}的時間需要{}到什麼時候呢？".format(resultDICT["class_arrangement"]["Course/Student"],resultDICT["class_arrangement"]["EarlyOrLate"])
                                    else:
                                        replySTR="好的，\n{}的時間{} {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["Course/Student"],resultDICT["class_arrangement"]["EarlyOrLate"],resultDICT["class_arrangement"]["AlterTimeSpan"])
                            else:
                                if resultDICT["class_arrangement"]["EarlyOrLate"] == "unknown":
                                    replySTR="好的，\n{}的時間改到 {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["Course/Student"],resultDICT["class_arrangement"]["AlterTime"])
                                else:
                                    replySTR="好的，\n{}的時間{}到 {}。\n麻煩您確認一下這樣對嗎？".format(resultDICT["class_arrangement"]["Course/Student"],resultDICT["class_arrangement"]["EarlyOrLate"],resultDICT["class_arrangement"]["AlterTime"])                            
                        self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"] = resultDICT["class_arrangement"]
                    elif "warm_blessing" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        self.mscDICT[self.user.id]["savedIntent"]="warm_blessing"
                        if resultDICT["warm_blessing"]["Holiday"] == "unknown":
                            replySTR = "謝謝您的祝福！ 祝您事事順心！"
                        else: 
                            replySTR = "謝謝您的祝福！也祝您{}快樂喔！".format(resultDICT["warm_blessing"]["Holiday"])
                    elif "physical_course" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        self.mscDICT[self.user.id]["savedIntent"]="physical_course"
                        replySTR = "好的，下次課程恢復實體喔！\n已轉告老師，感謝您！"
                    elif "online_course" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        self.mscDICT[self.user.id]["savedIntent"]="online_course"
                        replySTR = "好的，下次課程改為線上喔！\n已轉告老師，感謝您！"
                    elif "agree" in resultDICT["intentLIST"]:
                        #replySTR = resultDICT
                        if "day_off" in self.mscDICT[self.user.id]["savedIntent"]:
                            if self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["Course/Student"] == "unknown":
                                if self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelDate"] == "unknown":
                                    replySTR = "課程異動通知：\n{}{}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelTimeText"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelKeyword"])
                                else:
                                    replySTR = "課程異動通知：\n{} {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelDate"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelKeyword"])
                            else:
                                if self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelDate"] == "unknown":
                                    replySTR = "課程異動通知：\n{}{}{}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["Course/Student"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelTimeText"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelKeyword"],)
                                else:
                                    replySTR = "課程異動通知：\n{} {} {}。\n已轉告老師，感謝您!".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["Course/Student"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelDate"],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["CancelKeyword"])
                        elif "class_arrangement" in self.mscDICT[self.user.id]["savedIntent"]:
                            #replySTR = self.mscDICT[self.user.id]
                            if self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["Course/Student"] == "unknown" or self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["Course/Student"] == "":
                                if self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"] == "unknown":
                                    replySTR = "課程異動通知：\n課程時間{} {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTimeSpan"])
                                else: 
                                    if self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"]=="unknown":
                                        replySTR = "課程異動通知：\n課程時間改到 {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"])
                                    else:
                                        replySTR = "課程異動通知：\n課程時間{}到 {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"])
                            else:
                                if self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"] == "unknown":
                                    replySTR = "課程異動通知：\n{}的時間{}{}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["Course/Student"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTimeSpan"])
                                else: 
                                    if self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"]=="unknown":
                                        replySTR = "課程異動通知：\n{}的時間改到 {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["Course/Student"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"])
                                    else:
                                        replySTR = "課程異動通知：\n{}的時間{}到 {}。\n已轉告老師，感謝您！".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["Course/Student"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["EarlyOrLate"],self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]["AlterTime"])                                
                        elif "online_course" in self.mscDICT[self.user.id]["savedIntent"]:
                            replySTR = "課程異動通知：\n 課程改為線上授課\n已轉告老師，感謝您！"
                        elif "physical_course" in self.mscDICT[self.user.id]["savedIntent"]:
                            replySTR = "課程異動通知：\n 課程恢復實體授課\n已轉告老師，感謝您！"
                        self.mscDICT[self.user.id] = {"updatetime" : None,
                                                      "latestQuest": "",
                                                      "savedIntent":"",
                                                      "msgSTR":"",
                                                      "requiredInfo":{}
                                                      }
                    elif "disagree" in resultDICT["intentLIST"]:
                        if "day_off" in self.mscDICT[self.user.id]["savedIntent"]:
                            replySTR = "抱歉，能請您再用中文輸入一次要請假的日期嗎？\n(Bot Assistant 可能尚未學習到以上句型，若您想要請假，您可以說：「王小明八月八日英文課請假。」)"
                        elif "class_arrangement" in self.mscDICT[self.user.id]["savedIntent"]:
                            replySTR = "抱歉，能請您再用中文輸入一次要調課到哪天嗎？\n(Bot Assistant 可能尚未學習到以上句型，若您想要調課，您可以說：「王小明的英文課改到八月十日。」)"
                        elif "physical_course" in self.mscDICT[self.user.id]["savedIntent"] or "online_course" in self.mscDICT[self.user.id]["savedIntent"]:
                            replySTR = "抱歉，能請您再用中文輸入一次嗎？\n(Bot Assistant 可能尚未學習到以上句型，若您想要調整上課方式，您可以說：「明天英文課改線上上課或是實體授課。」)"
                        else:
                            replySTR = "抱歉，Bot Assistant 可能尚未學習到以上句型。\n若您想要請假，您可以說：「王小明八月八日英文課請假。」\n若您想要調課，您可以說：「王小明今天的英文課改到八月十日。」\n若您想要調整上課方式，您可以說：「改成線上上課」或是「恢復實體授課」。"
                    elif "inform_time" in resultDICT["intentLIST"]:
                        self.mscDICT[message.author.id]["lastInfoQuest"] = msgSTR
                        if "day_off" in self.mscDICT[self.user.id]["savedIntent"]:
                            self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['CancelDate'] = resultDICT["inform_time"]["inform_time_time"]
                            if self.mscDICT[self.user.id]["requiredInfo"]["day_off"]["Course/Student"] == "unknown":
                                replySTR = "好的，\n{} {}。\n麻煩您確認一下這樣對嗎？".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['CancelDate'],self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['CancelKeyword'])
                            else:
                                replySTR = "好的，\n{} {} {}。\n麻煩您確認一下這樣對嗎？".format(self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['Course/Student'], self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['CancelDate'], self.mscDICT[self.user.id]["requiredInfo"]["day_off"]['CancelKeyword'])
                        elif "class_arrangement" in self.mscDICT[self.user.id]["savedIntent"]:
                            #replySTR = resultDICT["inform_time"]["inform_time_time"]
                            self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]['AlterTime'] = resultDICT["inform_time"]["inform_time_time"]
                            replySTR="好的，\n課程時間改到 {}。\n麻煩您確認一下這樣對嗎？".format(self.mscDICT[self.user.id]["requiredInfo"]["class_arrangement"]['AlterTime'])
                else:
                    replySTR ="感謝您的告知，此次問題 Bot Assistant 較無法處理，為保險起見，會請老師看過後盡速回覆!\n若您想要請假，您可以說：「王小明八月八日英文課請假。」\n若您想要調課，您可以說：「王小明的英文課改到八月十日。」\n若您想要調整上課方式，您可以說：「改成線上上課」或是「恢復實體授課」。"
            self.mscDICT[self.user.id]["latestQuest"] = replySTR
        await message.reply(replySTR)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])