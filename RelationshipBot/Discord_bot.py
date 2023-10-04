#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
import random
from datetime import datetime
from pprint import pprint
import sys

sys.path.append('/family')
sys.path.append('/life_style')
sys.path.append('/loyalty')
sys.path.append('/money')
sys.path.append('/personality')
sys.path.append('/sex')

import family.family
import life_style.life_style
import loyalty.loyalty
import money.money
import personality.personality
import sex.sex
import pingying_preprocessing.pingying_preprocessing

logging.basicConfig(level=logging.DEBUG)


punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";","."]
    resultDICT_family = family.family.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_life_style = life_style.life_style.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_money = money.money.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_personality = personality.personality.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_sex = sex.sex.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    resultDICT_loyalty = loyalty.loyalty.execLoki(inputLIST, filterLIST=filterLIST, splitLIST=splitLIST)
    logging.debug("Loki Result family => {}".format(resultDICT_family))
    logging.debug("Loki Result life_style => {}".format(resultDICT_life_style))
    logging.debug("Loki Result money => {}".format(resultDICT_money))
    logging.debug("Loki Result personality => {}".format(resultDICT_personality))
    logging.debug("Loki Result sex => {}".format(resultDICT_sex))
    logging.debug("Loki Result loyalty => {}".format(resultDICT_loyalty))
    return resultDICT_family,resultDICT_life_style,resultDICT_money,resultDICT_personality,resultDICT_sex,resultDICT_loyalty

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = {    "id": messageAuthorID,
                            "updatetime" : datetime.now(),
                            "latestQuest": "",
                            "false_count" : 0,
                            "hi_count" : 0,
                            "bye_count": 0,
                            "thx_count": 0,
                            "Q_count" : 0
        }
        return templateDICT
    
    def choose_reply(self,replySTR,type):
        replyDICT = (
            "看來有關{}的問題困擾著你啊🤔~試試看這樣處理如何:\n\n",
            "我了解你有關{}的困擾了，別擔心🤗~先試試這樣處理:\n\n",
            "這的確是{}中挺棘手的問題呢🤔!不過先試試這樣處理怎麼樣:\n\n",
            "來，先跟我深呼吸，吸~吐~做得好👍!先試試看用以下方法處理有關{}的問題:\n\n",
            "處理{}的問題並不簡單，希望下面的方法可以幫到你!🤗:\n\n"
        )
        replySTR = replySTR + replyDICT[random.randint(0,4)].format(type)
        return replySTR
    
    def choose_conclusion(self,replySTR):
        replyDICT = (
            "上面的回覆只是給泥參考而已，如果不4合ㄉ話霸偷不要罵偶😣，偶會桑心😢",
            "咳咳，現在發表免責聲明:請自行判斷上述建議是否合適，若必要，請尋求專業人士的協助😐",
            "",
            "如果你真的覺得累了，有時候分手也是一種解脫喔~\n🎵分手快樂~祝你快樂~你可以找到更好的~🎵",
            "希望你可以順利解決問題~我會幫你加油的!✺◟(＾∇＾)◞✺"
        )
        replySTR = replySTR + replyDICT[random.randint(0,4)].format(type)
        return replySTR

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.mscDICT = {
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

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
            
# ##########初次對話：這裡是 keyword trigger 的。
            if msgSTR.lower() in ["哈囉","嗨","你好","妳好","您好","hi","hello","yo","安","hey","在嘛","在嗎","在嬤","嘿","sup"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，你太久沒跟我說話，我還以為你不要我了😢"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        if self.mscDICT[message.author.id]["hi_count"] < 4:
                            replySTR = "你剛剛才跟我嗨過喔~你忘記了嗎?"
                            self.mscDICT[message.author.id]["hi_count"] += 1
                        else:
                            replySTR = "你煩不煩啊？有甚麼問題快問啦！😠你是被另一伴說金魚腦所以才來這裡取暖是不是？？？🤨"
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "嗨嗨~我是感情小助理🙂~\n可以協助您解決感情世界的疑難雜症~\n您可以試著問我有關男女朋友之間的煩惱\n"
                    self.mscDICT[message.author.id]["hi_count"] += 1
            
            elif msgSTR.lower() in ["掰","掰掰","bye","晚安","goodbye","掰囉","byebye","bye bye","good night","gn","night","night night","滾"]:
                if message.author.id not in self.mscDICT.keys() or self.mscDICT[message.author.id]["Q_count"] == 0:
                    replySTR = "你甚麼都還沒問到欸?真的要走了?" 
                else :
                    if self.mscDICT[message.author.id]["bye_count"] == 0:
                        replySTR = "掰掰~希望我今天有幫到你，之後有甚麼煩惱都可以隨時跟我說喔!🤗"
                        self.mscDICT[message.author.id]["bye_count"] += 1
                    elif self.mscDICT[message.author.id]["bye_count"] < 4:
                        replySTR = "你剛剛才跟我掰掰過喔~你忘記了嗎?趕緊去忙吧~"
                        self.mscDICT[message.author.id]["bye_count"] += 1
                    else :
                        replySTR = "是要掰幾次啦???我都不用休息???不要在這裡浪費生命好不好😠"
                        
            elif msgSTR.lower() in ["謝啦","謝謝你","謝謝妳","感謝你","感謝妳","thank you","thanks","thankyou","感謝","thx","謝謝"]:
                if message.author.id not in self.mscDICT.keys() or self.mscDICT[message.author.id]["Q_count"] == 0 :
                    replySTR = "雖然不太清楚我幫了你甚麼，但不客氣~😎" 
                else :
                    if self.mscDICT[message.author.id]["thx_count"] == 0:
                        replySTR = "不用客氣啦!希望有幫到你，還有任何煩惱都可以跟我說喔!🤗"
                        self.mscDICT[message.author.id]["thx_count"] += 1
                    elif self.mscDICT[message.author.id]["thx_count"] < 4:
                        replySTR = "不用謝那麼多次啦~我會害羞😊"
                        self.mscDICT[message.author.id]["thx_count"] += 1
                    else :
                        replySTR = "不 客 氣。"
            elif msgSTR.lower() in ["對不起","抱歉","sor","sorry","拍謝","我錯了","我的錯","不要生氣啦","對不起啦"]:
                if  message.author.id not in self.mscDICT.keys() or (self.mscDICT[message.author.id]["false_count"] < 4 and self.mscDICT[message.author.id]["bye_count"] < 4 and self.mscDICT[message.author.id]["thx_count"] < 4 and self.mscDICT[message.author.id]["hi_count"] < 4) :
                    replySTR = "怎麼突然道歉了?你沒做錯甚麼事啊~"
                else:
                    replySTR = "知錯能改，善莫大焉!我這次就原諒你吧~"
# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                if message.author.id not in self.mscDICT.keys():
                   self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";","."]
                print("MSG:",msgSTR)
                resultDICT_pre = pingying_preprocessing.pingying_preprocessing.execLoki(msgSTR,splitLIST=splitLIST)
                if "correct" in resultDICT_pre:
                    msgSTR = resultDICT_pre["correct"][0]
                    logging.debug("Loki Result preprocessing => {}".format(resultDICT_pre))
                resultDICT_family,resultDICT_life_style,resultDICT_money,resultDICT_personality,resultDICT_sex,resultDICT_loyalty = getLokiResult(msgSTR)
                resultDICT_pre.clear()
                logging.debug("######\nLoki 處理結果如下：")
                replySTR = ""
                reply = False
                if "response" in resultDICT_family:
                    replySTR = self.choose_reply(replySTR,"家庭")
                    for i in range(len(resultDICT_family["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_family["response"][i] + "\n\n"
                    resultDICT_family.clear()
                    reply = True
                if "response" in resultDICT_life_style:
                    replySTR = self.choose_reply(replySTR,"生活習慣")
                    for i in range(len(resultDICT_life_style["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_life_style["response"][i] + "\n\n"
                    resultDICT_life_style.clear()
                    reply = True
                if "response" in resultDICT_money:
                    replySTR = self.choose_reply(replySTR,"經濟")
                    for i in range(len(resultDICT_money["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_money["response"][i] + "\n\n"
                    resultDICT_money.clear()
                    reply = True
                if "response" in resultDICT_personality:
                    replySTR = self.choose_reply(replySTR,"個性")
                    for i in range(len(resultDICT_personality["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_personality["response"][i] + "\n\n"
                    resultDICT_personality.clear()
                    reply = True
                if "response" in resultDICT_sex:
                    replySTR = self.choose_reply(replySTR,"性事")
                    for i in range(len(resultDICT_sex["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_sex["response"][i] + "\n\n"
                    resultDICT_sex.clear()
                    reply = True
                if "response" in resultDICT_loyalty:
                    replySTR = self.choose_reply(replySTR,"忠誠")
                    for i in range(len(resultDICT_loyalty["response"])):
                        replySTR = replySTR +str(i+1)+". "+resultDICT_loyalty["response"][i] + "\n\n"
                    resultDICT_loyalty.clear()
                    reply = True
                if reply == False:
                    self.mscDICT[message.author.id]["false_count"] += 1
                    if self.mscDICT[message.author.id]["false_count"] == 1:
                        replySTR = "很抱歉，我不太理解您的意思，您可以試著問我有關:\n1.家庭\n2.經濟\n3.個性\n4.生活習慣\n5.性事\n6.忠誠\n 以上6種方面的問題喔~"
                    elif self.mscDICT[message.author.id]["false_count"] >= 5:
                        replySTR = "夠了沒啦😠，就說聽不懂了😤"
                    else:
                        replySTR = "很抱歉，我還是不太理解您的意思，可能是您的狀況比較特殊，我暫時沒有辦法處理😢"
                else:
                    self.mscDICT[message.author.id]["false_count"] = 0
                    self.mscDICT[message.author.id]["thx_count"] = 0
                    self.mscDICT[message.author.id]["bye_count"] = 0
                    self.mscDICT[message.author.id]["Q_count"] += 1
                    replySTR = self.choose_conclusion(replySTR)
                    # replySTR = replySTR + "\n\n請注意，以上回覆僅供參考，請自行評估問題的嚴重性以尋求專業人士的協助。"
            await message.reply(replySTR)
            
if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
