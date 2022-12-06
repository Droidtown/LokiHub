#!/user/bin/env python
# -*- coding: utf-8 -*-

from ArticutAPI import Articut
import cn2num
import datetime
import discord
from FitBoty import runLoki
import json
import logging
from pprint import pprint
import re


logging.basicConfig(level=logging.DEBUG)


with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])

with open("sports_dict.json", encoding="utf-8") as f: #讀取account.info
    sports_dict = json.loads(f.read())

punctuationPat = re.compile("[,\?:;，。？、：；\n]+")
def getLokiResult(inputSTR, filterLIST):
    punctuationPat = re.compile("[,\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result



class BotClient(discord.Client):
    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.datetime.now()
        return templateDICT

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"gender": None,
                             "age":None,
                             "height":None,
                             "weight":None,
                             "correct":None,
                             "incorrect":None,
                             "update_info":None,
                             "BMR":None,
                             "food_cal":None,
                             "sports_cal":None,
                             "updatetime": datetime.datetime.now(),
                             "filterLIST":[]
        }
        self.mscDICT = {

        }

        # ####################################################################################

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user: #message 是 human，user 是 bot
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
            if msgSTR == "ping": #用以測試 bot 是否可執行
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR="pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","安安","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)

                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    await message.reply("嗨嗨我是 FitBoty :)")
                    replySTR = "我會計算你每日攝取熱量與基礎代謝率之差值，並推薦你適合的運動項目。\n為了計算你的基礎代謝率，想請問你的生理性別是？"
                    self.mscDICT[message.author.id]["filterLIST"] = ["gender"]

# ##########非初次對話：這裡用 Loki 計算語意 (真正的邏輯應該寫在這)
            else: #開始處理正式對話

                        #use datetime to get current time.
                        #if before 12:00pm, ask breakfast
                        #if between 12pm to 7pm, ask breakfast and lunch
                        #if after 7pm, ask what are eaten in this day

                #從這裡開始接上 NLU 模型
                resultDICT = getLokiResult(msgSTR, self.mscDICT[message.author.id]["filterLIST"])
                print(resultDICT) #Loki 回來的結果
                
                for i in resultDICT.keys():
                    self.mscDICT[message.author.id][i] = resultDICT[i]
                    
                    if i == 'correct':
                        self.mscDICT[message.author.id]["correct"] = resultDICT["correct"]
                        if self.mscDICT[message.author.id]["gender"] == "男性":
                            BMR = 66 + (13.7 * self.mscDICT[message.author.id]["weight"] + 5 * self.mscDICT[message.author.id]["height"] - 6.8 * self.mscDICT[message.author.id]["age"])
                            await message.reply("你的基礎代謝率為 " + str(BMR) + " 卡" + "。")
                            self.mscDICT[message.author.id]["BMR"] = BMR
                        if  self.mscDICT[message.author.id]["gender"] == "女性":
                            BMR = 655 + (9.6 * self.mscDICT[message.author.id]["weight"] + 1.8 * self.mscDICT[message.author.id]["height"] - 4.7 * self.mscDICT[message.author.id]["age"])
                            self.mscDICT[message.author.id]["BMR"] = BMR
                            await message.reply("你的基礎代謝率為 " + str(self.mscDICT[message.author.id]["BMR"]) + " 卡" + "。")
                    elif i == "incorrect":
                        self.mscDICT[message.author.id]["incorrect"] = resultDICT["incorrect"]
                    else: 
                        pass
                
                
                if self.mscDICT[message.author.id]["gender"] == None:
                    replySTR = "請問你的生理性別是？"
                    self.mscDICT[message.author.id]["filterLIST"] = ["gender"]
                elif self.mscDICT[message.author.id]["age"] == None:   
                    replySTR = "你今年幾歲呢？"
                    self.mscDICT[message.author.id]["filterLIST"] = ["age"]
                elif self.mscDICT[message.author.id]["height"] == None:
                    replySTR = "你身高幾公分？"
                    self.mscDICT[message.author.id]["filterLIST"] = ["height"]
                elif self.mscDICT[message.author.id]["weight"] == None:
                    replySTR = "你體重幾公斤"
                    self.mscDICT[message.author.id]["filterLIST"] = ["weight"]
                elif self.mscDICT[message.author.id]["correct"] == None and self.mscDICT[message.author.id]["incorrect"] == None:
                    replySTR = self.mscDICT[message.author.id]["gender"] + "\n" + str(self.mscDICT[message.author.id]["age"]) + "歲" + "\n" + str(self.mscDICT[message.author.id]["height"]) + "公分" + "\n" + str(self.mscDICT[message.author.id]["weight"]) + "公斤" + "\n" + "請確認以上資料是否正確？"
                    self.mscDICT[message.author.id]["filterLIST"] = ["correct", "incorrect", "update_info"]
                elif self.mscDICT[message.author.id]["incorrect"] != None and self.mscDICT[message.author.id]["update_info"] == None:
                    replySTR = "請問哪一項資料錯誤？" 
                    self.mscDICT[message.author.id]["filterLIST"] = ["update_info"]
                elif self.mscDICT[message.author.id]["update_info"] != None:
                    if self.mscDICT[message.author.id]["update_info"] == self.mscDICT[message.author.id]["age"]:
                        self.mscDICT[message.author.id].update({"age": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的年齡是幾歲？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["age"]
                    elif self.mscDICT[message.author.id]["update_info"] == self.mscDICT[message.author.id]["height"]:
                        self.mscDICT[message.author.id].update({"height": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的身高是多少？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["height"]
                    elif self.mscDICT[message.author.id]["update_info"] == self.mscDICT[message.author.id]["weight"]:
                        self.mscDICT[message.author.id].update({"weight": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的體重是多少？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["weight"]
                    elif self.mscDICT[message.author.id]["update_info"] == "性別":
                        self.mscDICT[message.author.id].update({"gender": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的性別為何？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["gender"]
                    elif self.mscDICT[message.author.id]["update_info"] == "年齡":
                        self.mscDICT[message.author.id].update({"age": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的年齡是幾歲？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["age"]
                    elif self.mscDICT[message.author.id]["update_info"] == "身高":
                        self.mscDICT[message.author.id].update({"height": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的身高是多少？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["height"]
                    elif self.mscDICT[message.author.id]["update_info"] == "體重":
                        self.mscDICT[message.author.id].update({"weight": None, 'correct': None, 'incorrect': None, 'update_info':None})
                        replySTR = "你正確的體重是多少？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["weight"]
                else:
                    pass

                
                
                if self.mscDICT[message.author.id]["BMR"] != None and self.mscDICT[message.author.id]["food_cal"] == None:
                    if int(datetime.datetime.now().strftime('%H')) >= 5 and int(datetime.datetime.now().strftime('%H')) < 12:
                        replySTR = "你早餐吃了什麼呢？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["food"]
                    elif int(datetime.datetime.now().strftime('%H')) >= 12 and int(datetime.datetime.now().strftime('%H')) < 19:
                        replySTR = "你早餐和午餐吃了什麼呢？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["food"]
                    elif int(datetime.datetime.now().strftime('%H')) >= 19 and int(datetime.datetime.now().strftime('%H')) <= 23:
                        replySTR = "你今天三餐吃了些什麼呢？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["food"]
                    elif int(datetime.datetime.now().strftime('%H')) >= 0 or int(datetime.datetime.now().strftime('%H')) < 5:
                        replySTR = "消夜吃了什麼呢？"
                        self.mscDICT[message.author.id]["filterLIST"] = ["food"]

                if self.mscDICT[message.author.id]["BMR"] != None:
                    #resultDICT = getLokiResult(msgSTR)
                    for i in resultDICT.keys():
                        if i == "food_cal":
                            self.mscDICT[message.author.id]["food_cal"] = sum(resultDICT["food_cal"])
                            if self.mscDICT[message.author.id]["food_cal"] == 0:
                                replySTR = "很抱歉，我無法估計你的進食熱量，在此先以 0 卡計算" + "。\n" + "請問你今天做了什麼運動且做了多久呢？"
                                self.mscDICT[message.author.id]["filterLIST"] = ["sports"]
                            else:
                                replySTR = "總共攝入" + str(self.mscDICT[message.author.id]["food_cal"]) + "卡" + "。\n" + "請問你今天做了什麼運動且做了多久呢？"
                                self.mscDICT[message.author.id]["filterLIST"] = ["sports"]

                        if i == "sports_cal":
                            try:
                                self.mscDICT[message.author.id]["sports_cal"] = sum(resultDICT["sports_cal"])
                                if self.mscDICT[message.author.id]["sports_cal"] == int("0"):
                                    today_cal = self.mscDICT[message.author.id]["BMR"] - float(self.mscDICT[message.author.id]["food_cal"])
                                    await message.reply("很抱歉，我無法估計你的運動熱量，在此先以 0 卡計算。")
                                else:
                                    today_cal = self.mscDICT[message.author.id]["BMR"] - float(self.mscDICT[message.author.id]["food_cal"]) + float(self.mscDICT[message.author.id]["sports_cal"])

                                sports_keyLIST = list(sports_dict.keys())
                                sports_valLIST = list(sports_dict.values())
                                if today_cal >= 0:
                                    rec_sportsSTR = '、'.join([str(s) for s in sports_keyLIST])
                                    replySTR = "你今天消耗的熱量比攝入還要多" + str(today_cal) + "卡。\n恭喜你離你的目標又更近了一步！如果還有餘力，也推薦你可以做以下運動喔：\n" + rec_sportsSTR + "任一項進行10分鐘。"
                                else:
                                    rec_sportsLIST1 = []
                                    rec_sportsLIST2 = []
                                    rec_sportsLIST3 = []
                                    rec_sportsLIST4 = []
                                    for j in sports_valLIST:
                                        if today_cal*-1 <= j*10:
                                            rec_sports1 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports1:
                                                rec_sportsLIST1.append(i)
                                        else:
                                            pass
                                        if today_cal*-1 > j*10 and today_cal*-1 <= j*20:
                                            rec_sports2 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports2:
                                                rec_sportsLIST2.append(i)
                                        else:
                                            pass
                                        if today_cal*-1 > j*20 and today_cal*-1 <= j*30:
                                            rec_sports3 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports3:
                                                rec_sportsLIST3.append(i)
                                        else:
                                            pass
                                        if today_cal*-1 > j*30:
                                            rec_sports4 = [k for k,v in sports_dict.items() if v == j]
                                            for i in rec_sports4:
                                                rec_sportsLIST4.append(i)
                                        else:
                                            pass

                                    if rec_sportsLIST1 != []:
                                        rec_sportsSTR1 = '、'.join([str(s) for s in set(rec_sportsLIST1)])
                                        rec_10min = rec_sportsSTR1 + "任一項進行10分鐘。\n"
                                    else:
                                        rec_10min = ""
                                    if rec_sportsLIST2 != []:
                                        rec_sportsSTR2 = '、'.join([str(s) for s in set(rec_sportsLIST2)])
                                        rec_20min = rec_sportsSTR2 + "任一項進行20分鐘。\n"
                                    else:
                                        rec_20min = ""
                                    if rec_sportsLIST3 != []:
                                        rec_sportsSTR3 = '、'.join([str(s) for s in set(rec_sportsLIST3)])
                                        rec_30min = rec_sportsSTR3 + "任一項進行30分鐘。\n"
                                    else:
                                        rec_30min = ""
                                    if rec_sportsLIST4 != []:
                                        rec_sportsSTR4 = '、'.join([str(s) for s in set(rec_sportsLIST4)])
                                        rec_50min = rec_sportsSTR4 + "任一項進行50分鐘。\n"
                                    else:
                                        rec_50min = ""

                                    replySTR = "你今天攝入的熱量比消耗還要多" + str(today_cal) + "卡。\n推薦你可以做以下運動消耗今日剩餘的熱量喔：\n" + rec_10min + rec_20min + rec_30min + rec_50min
                            except TypeError:
                                print("sportcal type error")
                                #pass



                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)


            print(self.mscDICT)
            await message.reply(replySTR) #機器人統一回覆



if __name__ == "__main__":
    #client = BotClient()
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])