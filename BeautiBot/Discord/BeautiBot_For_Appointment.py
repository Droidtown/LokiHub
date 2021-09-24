#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint

from BeautiBot_Loki import result as beautiBot
from botREF import handleBodypartDICT
from botREF import userDefinedDICT

logging.basicConfig(level=logging.INFO) 

# <取得多輪對話資訊>
client = discord.Client()

mscDICT = {
}
appointmentLIST = []

# </取得多輪對話資訊>

with open("account.info.py", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))

@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    #if message.channel.name != "dt_intern":
        #return

    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return
    
    # Greetings
    try:
        print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
        msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
        logging.info(msgSTR)
        #print("msgSTR =", msgSTR)
        replySTR = ""    # Bot 回應訊息

        if re.search("(hi|hello|hey|yo|哈囉|嗨|嗨嗨|[你您]好|在嗎|早安|午安|晚安|早上好|晚上好|欸|誒|ㄟ)", msgSTR.lower()):
            replySTR = "嗨嗨，你需要什麼除毛相關的醫美服務呢？\n可以跟我說「我想除毛」或是「我想預約星期一下午ＯＯＯ醫師的除毛門診」喔^_^\n\n*小提醒：我目前只看得懂中文喔～*"
            await message.reply(replySTR)
            return
    except Exception as e:
        logging.error("[MSG greetings ERROR] {}".format(str(e)))
    
    
    lokiResultDICT = beautiBot(msgSTR)    # 取得 Loki 回傳結果
    logging.info(lokiResultDICT)  
    
    # 多輪對話
    try:
        if lokiResultDICT:
            if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
                mscDICT[client.user.id] = {"bodypart": None,
                                           "request": "",
                                           "confirm": "",
                                           "queryIntentSTR": "",
                                           "bodyQuestionSTR": "",
                                           "appointmentQuestionSTR": "",
                                           "appointmentClinic": "",
                                           "appointmentDoctor": "",
                                           "appointmentDay": "",
                                           "appointmentTime": "",
                                           "medicalHistory": "",
                                           "updatetime": datetime.now(),
                                           "finish": ""
                                           }  
                #logging.info(mscDICT)
            else: 
                # 處理時間差
                datetimeNow = datetime.now()  # 取得當下時間
                timeDIFF = datetimeNow - mscDICT[client.user.id]["updatetime"]
                if timeDIFF.total_seconds() <= 300:    # 以秒為單位，5分鐘以內都算是舊對話
                    mscDICT[client.user.id]["updatetime"] = datetimeNow
                    
                # 先處理「簡答題」
                    if mscDICT[client.user.id]["request"] == "" and mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodypart"] == None:
                        if "其他" in msgSTR and "部位": # ["請問有哪些部位可以除","請問可以除哪些部位","有哪些部位可以除","可以除哪些部位"]
                            replySTR = "目前沒有耶～要不要再考慮一下我們目前可以處理的部位呢？\n【全臉｜鬍子｜眉心｜唇周｜下巴｜前頸｜後頸｜胸部｜乳暈｜腋下｜手臂｜手指｜手背｜全手｜腹部｜子母線｜背部｜私密處｜臀部｜小腿｜大腿｜膝蓋｜腳｜腳趾｜腳背】"                   
                    
                    # 改預約時間、診所、醫師
                    elif mscDICT[client.user.id]["appointmentQuestionSTR"] == None:
                        if any(e in msgSTR for e in ["對","正確","沒錯"]):
                            QlokiResultDICT = beautiBot(msgSTR, ["confirm"])
                            logging.info(QlokiResultDICT)    
                            mscDICT[client.user.id]["finish"] = QlokiResultDICT["confirm"]
                            
                        elif "不" in msgSTR:
                            QlokiResultDICT = beautiBot(msgSTR, ["confirm"])
                            logging.info(QlokiResultDICT) 
                            mscDICT[client.user.id]["finish"] = QlokiResultDICT["confirm"]
                            
                        elif "改" in msgSTR and any(e in msgSTR for e in ["醫師","醫生"]):
                            QlokiResultDICT = beautiBot(msgSTR, ["appointmentDoctor"])
                            logging.info(QlokiResultDICT) 
                            if QlokiResultDICT["appointmentDoctor"] in ["王小明","程小剛","劉小美","謝小華","薛小強","陳小弘"]:
                                print(QlokiResultDICT["appointmentDoctor"])
                                mscDICT[client.user.id]["appointmentDoctor"] = QlokiResultDICT["appointmentDoctor"] 
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = ""
                            else:
                                replySTR = "請重新選擇醫師～\n【王小明醫師｜程小剛醫師｜謝小華醫師｜薛小強醫師｜陳小弘醫師｜劉小美醫師】"  
                                
                        elif "改" in msgSTR and "診所" in msgSTR:
                            QlokiResultDICT = beautiBot(msgSTR, ["appointmentClinic"])
                            logging.info(QlokiResultDICT) 
                            if QlokiResultDICT["appointmentClinic"] in userDefinedDICT["location"]:
                                mscDICT[client.user.id]["appointmentClinic"] = QlokiResultDICT["appointmentClinic"]  
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = ""
                            else:
                                replySTR = "請重新選擇診所～\ｎ【忠孝敦化診所｜南西診所】"  
                                
                        elif any(e in msgSTR for e in ["一","二","三","四","五","六"]) and "改" in msgSTR:
                            QlokiResultDICT = beautiBot(msgSTR, ["appointmentTime"])
                            logging.info(QlokiResultDICT) 
                            if QlokiResultDICT["appointmentDay"] != False and QlokiResultDICT["appointmentTime"] != False:
                                mscDICT[client.user.id]["appointmentDay"] = QlokiResultDICT["appointmentDay"]
                                mscDICT[client.user.id]["appointmentTime"] = QlokiResultDICT["appointmentTime"]  
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = ""
                            elif QlokiResultDICT["appointmentDay"] == False and QlokiResultDICT["appointmentTime"] != False:
                                mscDICT[client.user.id]["appointmentDay"] = ""
                                mscDICT[client.user.id]["appointmentTime"] = QlokiResultDICT["appointmentTime"] 
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = ""
                            elif QlokiResultDICT["appointmentDay"] != False and QlokiResultDICT["appointmentTime"] == False:
                                mscDICT[client.user.id]["appointmentDay"] = QlokiResultDICT["appointmentDay"] 
                                mscDICT[client.user.id]["appointmentTime"] = ""
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = ""
                            else:
                                mscDICT[client.user.id]["appointmentDay"] = ""
                                mscDICT[client.user.id]["appointmentTime"] = ""                            

                    # 回答醫療史
                    elif mscDICT[client.user.id]["appointmentQuestionSTR"] == "medicalHistory":
                        #if "沒有" in msgSTR:
                            #mscDICT[client.user.id]["medicalHistory"] = False
                        if any(e in msgSTR for e in ["沒有很","不會很","不算很","沒有太","不會太","不算太","沒有非常"]) or msgSTR == "有":
                            mscDICT[client.user.id]["medicalHistory"] = True
                        elif any(e in msgSTR for e in ["沒","沒有"]) :
                            mscDICT[client.user.id]["medicalHistory"] = False                        
                        else:
                            QlokiResultDICT = beautiBot(msgSTR, [mscDICT[client.user.id]["appointmentQuestionSTR"]])
                            logging.info(QlokiResultDICT) 
                            if QlokiResultDICT["medicalHistory"] in userDefinedDICT["medicalCondition"]:
                                print(userDefinedDICT["medicalCondition"])
                                mscDICT[client.user.id]["medicalHistory"] = QlokiResultDICT["medicalHistory"]
                            else:
                                mscDICT[client.user.id]["medicalHistory"] = False #ideal
                    # 回答醫師
                    elif mscDICT[client.user.id]["appointmentQuestionSTR"] == "appointmentDoctor":
                        QlokiResultDICT = beautiBot(msgSTR, [mscDICT[client.user.id]["appointmentQuestionSTR"]])
                        logging.info(QlokiResultDICT) 
                        if QlokiResultDICT["appointmentDoctor"] in ["王小明","程小剛","劉小美","謝小華","薛小強","陳小弘"]:
                            mscDICT[client.user.id]["appointmentDoctor"] = QlokiResultDICT["appointmentDoctor"] 
                        else:
                            replySTR = "請重新選擇醫師～\n【王小明醫師｜程小剛醫師｜謝小華醫師｜薛小強醫師｜陳小弘醫師｜劉小美醫師】"
                    # 回答診所
                    elif mscDICT[client.user.id]["appointmentQuestionSTR"] == "appointmentClinic":
                        if any(e in msgSTR for e in ["隨便"]):
                            mscDICT[client.user.id]["appointmentClinic"] = "南西診所"
                        else:
                            QlokiResultDICT = beautiBot(msgSTR, [mscDICT[client.user.id]["appointmentQuestionSTR"]])
                            logging.info(QlokiResultDICT) 
                            if QlokiResultDICT["appointmentClinic"] in userDefinedDICT["location"]:
                                mscDICT[client.user.id]["appointmentClinic"] = QlokiResultDICT["appointmentClinic"]                         
                            else:
                                replySTR = "請重新選擇診所～\ｎ【忠孝敦化診所｜南西診所】"
                    # 回答預約時間
                    elif mscDICT[client.user.id]["appointmentQuestionSTR"] == "appointmentTime": 
                        QlokiResultDICT = beautiBot(msgSTR, [mscDICT[client.user.id]["appointmentQuestionSTR"]])
                        logging.info(QlokiResultDICT) 
                        if QlokiResultDICT["appointmentDay"] != False and QlokiResultDICT["appointmentTime"] != False:
                            mscDICT[client.user.id]["appointmentDay"] = QlokiResultDICT["appointmentDay"]
                            mscDICT[client.user.id]["appointmentTime"] = QlokiResultDICT["appointmentTime"]    
                        elif QlokiResultDICT["appointmentDay"] == False and QlokiResultDICT["appointmentTime"] != False:
                            mscDICT[client.user.id]["appointmentDay"] = ""
                            mscDICT[client.user.id]["appointmentTime"] = QlokiResultDICT["appointmentTime"] 
                        elif QlokiResultDICT["appointmentDay"] != False and QlokiResultDICT["appointmentTime"] == False:
                            mscDICT[client.user.id]["appointmentDay"] = QlokiResultDICT["appointmentDay"] 
                            mscDICT[client.user.id]["appointmentTime"] = ""
                        else:
                            mscDICT[client.user.id]["appointmentDay"] = ""
                            mscDICT[client.user.id]["appointmentTime"] = ""                            

                    elif mscDICT[client.user.id]["bodyQuestionSTR"]:
                        if mscDICT[client.user.id]["bodyQuestionSTR"] in list(["".join(value) for value in handleBodypartDICT.values()]):
                            for v in userDefinedDICT["bodypart"]:
                                if v in msgSTR:
                                    mscDICT[client.user.id]["bodypart"] = v
                                    mscDICT[client.user.id]["request"] = True  # 因為會問「請問是大腿還是小腿呢？」，代表前提request要成立
                                    mscDICT[client.user.id]["bodyQuestionSTR"] = None  # 處理完簡答題後，清除問題
                        else:
                            replySTR = "請重新輸入你的需求～"        

                # 再處理「是非題」
                    else:
                        QlokiResultDICT = beautiBot(msgSTR, [mscDICT[client.user.id]["queryIntentSTR"]])
                        logging.info(QlokiResultDICT) 
                        
                        # inputSTR是「不對、沒有...」
                        if QlokiResultDICT["confirm"] == False:
                            # 確認醫療史沒問題 or 確認預約單
                            if mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != None and mscDICT[client.user.id]["confirm"] == True: 
                                if mscDICT[client.user.id]["finish"] == None or mscDICT[client.user.id]["finish"] == "":
                                    mscDICT[client.user.id]["finish"] = False 
                                elif mscDICT[client.user.id]["appointmentQuestionSTR"] == "medicalHistory":
                                    mscDICT[client.user.id]["medicalHistory"] = False
                            
                            # 確認「沒問題呀，我就幫您安排{}的除毛療程囉，好不好？」
                            if mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != None and mscDICT[client.user.id]["confirm"] == "":
                                mscDICT[client.user.id]["confirm"] = False
                                #mscDICT[client.user.id]["finish"] = None                       
                        
                        # inputSTR是「對、有...」
                        elif QlokiResultDICT["confirm"] == True:
                            # 問題是「確認預約單」
                            if mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != None and mscDICT[client.user.id]["confirm"] == True:
                                if mscDICT[client.user.id]["appointmentClinic"] != "" and mscDICT[client.user.id]["appointmentDoctor"] != "" and mscDICT[client.user.id]["appointmentDay"] != "" and mscDICT[client.user.id]["appointmentTime"] != "":
                                    if mscDICT[client.user.id]["finish"] != True:
                                        mscDICT[client.user.id]["finish"] = True  
                                    else:
                                        pass
                            elif mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != None and mscDICT[client.user.id]["confirm"] == "":
                                mscDICT[client.user.id]["confirm"] = True                               
                        else:
                            pass
                        
            # 將第一輪對話 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
            for k in lokiResultDICT.keys():
                if k == "bodypart" and lokiResultDICT[k] != "" and lokiResultDICT[k] != None:
                    mscDICT[client.user.id]["bodypart"] = lokiResultDICT["bodypart"]
                if k == "request" and mscDICT[client.user.id][k] != True:
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
                if k == "confirm" and lokiResultDICT[k] == "":
                    mscDICT[client.user.id]["appointmentDoctor"] = lokiResultDICT["appointmentDoctor"]               
                if k == "appointmentDoctor":
                    if lokiResultDICT[k] == "":
                        pass
                    else:
                        mscDICT[client.user.id]["appointmentDoctor"] = lokiResultDICT["appointmentDoctor"]
                if k == "appointmentClinic":
                    if lokiResultDICT[k] == "":
                        pass
                    else:                    
                        mscDICT[client.user.id]["appointmentClinic"] = lokiResultDICT["appointmentClinic"]   
                if k == "appointmentDay":
                    if lokiResultDICT[k] == "":
                        pass
                    else:                    
                        mscDICT[client.user.id]["appointmentDay"] = lokiResultDICT["appointmentDay"]                    
                if k == "appointmentTime":
                    if lokiResultDICT[k] == "":
                        pass
                    else:                    
                        mscDICT[client.user.id]["appointmentTime"] = lokiResultDICT["appointmentTime"]               
                if k == "msg":
                    replySTR = lokiResultDICT[k]
         
        else:
            if any(e in msgSTR for e in ["都","可","隨便","隨意"]):
                if mscDICT[client.user.id]["appointmentDoctor"] == "":
                    mscDICT[client.user.id]["appointmentDoctor"] = "王小明"
                    mscDICT[client.user.id]["finish"] = ""
                elif mscDICT[client.user.id]["appointmentClinic"] == "":
                    mscDICT[client.user.id]["appointmentClinic"] = "南西"
                    mscDICT[client.user.id]["finish"] = ""
            else:
                replySTR = "請重新輸入～"
                    
    except Exception as e:
        logging.error("[MSG lokiResultDICT ERROR] {}".format(str(e)))


    # bot回覆
    try:
        if mscDICT[client.user.id]:
            # 多輪的回覆
            if mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] != "": #!= none
                if mscDICT[client.user.id]["confirm"] == True:
                    if mscDICT[client.user.id]["finish"] == True:
                #把預約資訊存到 appointmentLIST
                        appointmentLIST.append(mscDICT[client.user.id]) 
                        replySTR = "謝謝你使用BeautiBot！如果有療程相關問題，可以繼續問我們的醫美小幫手BeautiQuestion喔！\n期待再為你服務～"
                #清空 mscDICT
                        mscDICT[client.user.id] = {"bodypart": None,
                                                   "request": "",
                                                   "confirm": "",
                                                   "queryIntentSTR": "",
                                                   "bodyQuestionSTR": "",
                                                   "appointmentQuestionSTR": "",
                                                   "appointmentClinic": "",
                                                   "appointmentDoctor": "",
                                                   "appointmentDay": "",
                                                   "appointmentTime": "",
                                                   "medicalHistory": "",
                                                   "updatetime": datetime.now(),
                                                   "finish": ""
                                                   }   
                #確認療程後，詢問病史
                    elif mscDICT[client.user.id]["finish"] == "":
                        if mscDICT[client.user.id]["medicalHistory"] == "":
                            replySTR = "請問你有沒有以下病史或情況呢？\n【藥物過敏、凝血功能障礙、蟹足腫、免疫疾病、糖尿病、癲癇、懷孕、哺乳中、抗生素】"
                            mscDICT[client.user.id]["appointmentQuestionSTR"] = "medicalHistory"
                        elif mscDICT[client.user.id]["medicalHistory"] != "":
                            # 病史不適合做療程
                            if mscDICT[client.user.id]["medicalHistory"] != False:
                                replySTR = "這樣你可能不適合做這個療程耶，建議請先詢問你的醫生喔～謝謝你使用BeautiBot！"
                                mscDICT[client.user.id] = {"bodypart": None,
                                                           "request": "",
                                                           "confirm": "",
                                                           "queryIntentSTR": "",
                                                           "bodyQuestionSTR": "",
                                                           "appointmentQuestionSTR": "",
                                                           "appointmentClinic": "",
                                                           "appointmentDoctor": "",
                                                           "appointmentDay": "",
                                                           "appointmentTime": "",
                                                           "medicalHistory": "",
                                                           "updatetime": datetime.now(),
                                                           "finish": ""
                                                           }                            
                                #mscDICT[client.user.id]["appointmentQuestionSTR"] = "medicalHistory" 
                            # 確認沒有病史後，詢問醫師
                            elif mscDICT[client.user.id]["medicalHistory"] == False:
                                replySTR = "OK~你要預約哪位醫師呢？\n請選擇【王小明醫師｜程小剛醫師｜謝小華醫師｜薛小強醫師｜陳小弘醫師｜劉小美醫師】\n也可以回答【都可以】，由王小明醫師看診。\n女性顧客可以回答【女醫師】，由劉小美醫師看診。"
                                mscDICT[client.user.id]["appointmentQuestionSTR"] = "appointmentDoctor"
                            # 確認醫師後，詢問預約哪間診所
                                if mscDICT[client.user.id]["appointmentDoctor"] != "":
                                    replySTR = "你要預約哪間診所呢？請選擇\n【忠孝敦化診所｜南西診所】\n也可以回答【都可以】，在南西診所看診。"
                                    mscDICT[client.user.id]["appointmentQuestionSTR"] = "appointmentClinic" 
                            # 確認診所後，詢問預約時段
                                    if mscDICT[client.user.id]["appointmentClinic"] != "":
                                        replySTR = "你要預約哪個時段呢？請選擇\n【星期一 12:30~17:00、18:00~20:30\n星期二 12:30~17:00、18:00~20:30\n星期三 14:00~17:00、18:00~20:30\n星期四 12:30~17:00、18:00~20:30\n星期五 12:30~17:00、18:00~20:30\n星期六 12:30~17:00、18:00~20:30\n(星期日為診所休息日)】"
                                        mscDICT[client.user.id]["appointmentQuestionSTR"] = "appointmentTime" 
                            # 確認時段後，收尾        
                                        if mscDICT[client.user.id]["appointmentDay"] != False and mscDICT[client.user.id]["appointmentTime"] != False:
                                            replySTR = """你預約的是：\n{} {}\n{}診所 的 {}除毛療程\n由{}醫師看診\n請問這樣正確嗎？\n\n如果訂單需要做修改，可以跟我說「我想改ＯＯＯ醫師」或是「我想改下星期六12:00」，讓我更快知道你的需求喔！""".format(mscDICT[client.user.id]["appointmentDay"],
                                                                                                                                                                                                                                                                                                                                  mscDICT[client.user.id]["appointmentTime"],
                                                                                                                                                                                                                                                                                                                                  mscDICT[client.user.id]["appointmentClinic"],
                                                                                                                                                                                                                                                                                                                                  mscDICT[client.user.id]["bodypart"],
                                                                                                                                                                                                                                                                                                                                  mscDICT[client.user.id]["appointmentDoctor"]
                                                                                                                                                                                                                                                                                                                                  )
                                            mscDICT[client.user.id]["appointmentQuestionSTR"] = None
                                            mscDICT[client.user.id]["finish"] = ""
        
                                        elif mscDICT[client.user.id]["appointmentDay"] == False and mscDICT[client.user.id]["appointmentTime"] != False:
                                            replySTR = "請重新選擇日期！\n【星期一 12:30~17:00、18:00~20:30\n星期二 12:30~17:00、18:00~20:30\n星期三 14:00~17:00、18:00~20:30\n星期四 12:30~17:00、18:00~20:30\n星期五 12:30~17:00、18:00~20:30\n星期六 12:30~17:00、18:00~20:30\n(星期日為診所休息日)】"
                                            mscDICT[client.user.id]["appointmentQuestionSTR"] = "appointmentTime" 
                                        elif mscDICT[client.user.id]["appointmentDay"] != False and mscDICT[client.user.id]["appointmentTime"] == False:
                                            replySTR = "請重新選擇看診時間！\n【星期一 12:30~17:00、18:00~20:30\n星期二 12:30~17:00、18:00~20:30\n星期三 14:00~17:00、18:00~20:30\n星期四 12:30~17:00、18:00~20:30\n星期五 12:30~17:00、18:00~20:30\n星期六 12:30~17:00、18:00~20:30\n(星期日為診所休息日)】"   
                                            mscDICT[client.user.id]["appointmentQuestionSTR"] = "appointmentTime" 
                
                    elif mscDICT[client.user.id]["finish"] == False:
                        replySTR = "請問哪些資訊不正確呢？\n\n如果訂單需要做修改，可以跟我說「我想改ＯＯＯ醫師」或是「我想改下星期六12:00」，讓我更快知道你的需求喔！"
                        mscDICT[client.user.id]["appointmentQuestionSTR"] = None
                         
                elif mscDICT[client.user.id]["confirm"] == False:
                    if mscDICT[client.user.id]["finish"] == None:
                        replySTR = "請問哪些資訊不正確呢？"   # and then? 
                    if mscDICT[client.user.id]["finish"] == "":
                        replySTR = "看來你應該是改變心意了吧？再請你重新輸入需要的醫美服務喔！" 
                        mscDICT[client.user.id] = {"bodypart": None,
                                                   "request": "",
                                                   "confirm": "",
                                                   "queryIntentSTR": "",
                                                   "bodyQuestionSTR": "",
                                                   "appointmentQuestionSTR": "",
                                                   "appointmentClinic": "",
                                                   "appointmentDoctor": "",
                                                   "appointmentDay": "",
                                                   "appointmentTime": "",
                                                   "medicalHistory": "",
                                                   "updatetime": datetime.now(),
                                                   "finish": ""
                                                   }                     

            # 第一輪的回覆
                if mscDICT[client.user.id]["confirm"] == "":
                    if replySTR != "":
                        pass
                    else:
                        if mscDICT[client.user.id]["bodypart"] == None:
                            replySTR = "好哇！請問想處理哪個部位呢？\n\n目前我們的除毛療程提供以下部位服務～\n【全臉｜鬍子｜眉心｜唇周｜下巴｜前頸｜後頸｜胸部｜乳暈｜腋下｜手臂｜手指｜手背｜全手｜腹部｜子母線｜背部｜私密處｜臀部｜小腿｜大腿｜膝蓋｜腳｜腳趾｜腳背】"
                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                            
                        elif mscDICT[client.user.id]["bodypart"] != None:
                            if mscDICT[client.user.id]["bodyQuestionSTR"] == None:   # input == "我想要除腿的毛"
                                replySTR = "OK～請問你要詢問{}的亞歷山大除毛雷射療程，是嗎？".format(mscDICT[client.user.id]["bodypart"])
                                mscDICT[client.user.id]["queryIntentSTR"] = "confirm"
                    
                            elif mscDICT[client.user.id]["bodyQuestionSTR"] != None and mscDICT[client.user.id]["bodyQuestionSTR"] != "":   # input == "我想除毛"
                                if mscDICT[client.user.id]["bodypart"] not in [key for key in handleBodypartDICT.keys()]:
                                    replySTR = "沒問題呀，我就幫您安排{}的亞歷山大除毛雷射療程囉，好不好？".format(mscDICT[client.user.id]["bodypart"])
                                    mscDICT[client.user.id]["queryIntentSTR"] = "confirm"  
                                    mscDICT[client.user.id]["bodyQuestionSTR"] = ""
                                else:
                                    for e in handleBodypartDICT.keys():
                                        if mscDICT[client.user.id]["bodypart"] == e:
                                            replySTR = "".join(handleBodypartDICT[e])
                                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart" 
                                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                                    else:
                                        pass                
                    
                            elif mscDICT[client.user.id]["bodyQuestionSTR"] == "":     # input == "我想要除胸毛"
                                if mscDICT[client.user.id]["bodypart"] not in [key for key in handleBodypartDICT.keys()]:
                                    replySTR = "了解～請問你要詢問{}的除毛療程，是嗎？".format(mscDICT[client.user.id]["bodypart"])
                                    mscDICT[client.user.id]["queryIntentSTR"] = "confirm"  
                                else:
                                    for e in handleBodypartDICT.keys():
                                        if mscDICT[client.user.id]["bodypart"] == e:
                                            replySTR = "".join(handleBodypartDICT[e])
                                            mscDICT[client.user.id]["queryIntentSTR"] = "bodypart" 
                                            mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                                        else:
                                            pass                              

            elif mscDICT[client.user.id]["request"] == "" and mscDICT[client.user.id]["bodypart"] != "" and mscDICT[client.user.id]["bodypart"] != None:      # input == "我腿毛好長"
                if mscDICT[client.user.id]["confirm"] == "" and mscDICT[client.user.id]["bodyQuestionSTR"] == "":  
                    if mscDICT[client.user.id]["bodypart"] != "毛":
                        if mscDICT[client.user.id]["bodypart"] not in [key for key in handleBodypartDICT.keys()]:
                            replySTR = "請問你要詢問{}的除毛療程，是嗎？".format(mscDICT[client.user.id]["bodypart"])
                            mscDICT[client.user.id]["queryIntentSTR"] = "confirm"  
                        else:
                            for e in handleBodypartDICT.keys():
                                if mscDICT[client.user.id]["bodypart"] == e:
                                    replySTR = "".join(handleBodypartDICT[e])
                                    mscDICT[client.user.id]["queryIntentSTR"] = "bodypart" 
                                    mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                            else:
                                pass                        

                elif mscDICT[client.user.id]["confirm"] == False and mscDICT[client.user.id]["bodyQuestionSTR"] == "":
                    replySTR = "看來你應該是改變心意了吧？再請你重新輸入需要的醫美服務喔！" 
                    mscDICT[client.user.id] = {"bodypart": None,
                                               "request": "",
                                               "confirm": "",
                                               "queryIntentSTR": "",
                                               "bodyQuestionSTR": "",
                                               "appointmentQuestionSTR": "",
                                               "appointmentClinic": "",
                                               "appointmentDoctor": "",
                                               "appointmentDay": "",
                                               "appointmentTime": "",
                                               "medicalHistory": "",
                                               "updatetime": datetime.now(),
                                               "finish": ""
                                               }                      
                    
            elif mscDICT[client.user.id]["request"] == True and mscDICT[client.user.id]["bodypart"] == "":   # input == "我想除毛" or "我想預約星期一下午四點在南西診所給程小剛醫生除毛" 
                if mscDICT[client.user.id]["appointmentDoctor"] != "" or mscDICT[client.user.id]["appointmentClinic"] != "" or mscDICT[client.user.id]["appointmentDay"] != "" or mscDICT[client.user.id]["appointmentTime"] != "":
                    replySTR = "請問想除毛嗎？想處理哪個部位呢？\n\n目前我們的除毛療程提供以下部位服務～\n【全臉｜鬍子｜眉心｜唇周｜下巴｜前頸｜後頸｜胸部｜乳暈｜腋下｜手臂｜手指｜手背｜全手｜腹部｜子母線｜背部｜私密處｜臀部｜小腿｜大腿｜膝蓋｜腳｜腳趾｜腳背】"
                    mscDICT[client.user.id]["queryIntentSTR"] = "bodypart"
                    mscDICT[client.user.id]["bodyQuestionSTR"] = replySTR
                else:
                    replySTR = "拍謝，我們沒有提供這個部位的療程喔！再請你重新輸入需要的醫美服務～"
                    mscDICT[client.user.id] = {"bodypart": None,
                                               "request": "",
                                               "confirm": "",
                                               "queryIntentSTR": "",
                                               "bodyQuestionSTR": "",
                                               "appointmentQuestionSTR": "",
                                               "appointmentClinic": "",
                                               "appointmentDoctor": "",
                                               "appointmentDay": "",
                                               "appointmentTime": "",
                                               "medicalHistory": "",
                                               "updatetime": datetime.now(),
                                               "finish": ""
                                               }                    

            elif mscDICT[client.user.id]["request"] == "" and mscDICT[client.user.id]["confirm"] == "":
                if mscDICT[client.user.id]["bodypart"] == "":
                    replySTR = "不好意思，我們沒有提供這個部位的療程喔！再請你重新輸入需要的醫美服務～"
                    mscDICT[client.user.id] = {"bodypart": None,
                                               "request": "",
                                               "confirm": "",
                                               "queryIntentSTR": "",
                                               "bodyQuestionSTR": "",
                                               "appointmentQuestionSTR": "",
                                               "appointmentClinic": "",
                                               "appointmentDoctor": "",
                                               "appointmentDay": "",
                                               "appointmentTime": "",
                                               "medicalHistory": "",
                                               "updatetime": datetime.now(),
                                               "finish": ""
                                               }                   
                elif mscDICT[client.user.id]["bodypart"] == None:
                    if "哪" in msgSTR and "部位" in msgSTR and "除" in msgSTR: #if msgSTR in ["請問有哪些部位可以除","請問可以除哪些部位","有哪些部位可以除","可以除哪些部位"]:
                        replySTR = "目前我們的除毛療程提供以下部位服務～\n【全臉｜鬍子｜眉心｜唇周｜下巴｜前頸｜後頸｜胸部｜乳暈｜腋下｜手臂｜手指｜手背｜全手｜腹部｜子母線｜背部｜私密處｜臀部｜小腿｜大腿｜膝蓋｜腳｜腳趾｜腳背】"
                        mscDICT[client.user.id]["bodypart"] = None
                        mscDICT[client.user.id]["confirm"] = ""
                    elif "只" in msgSTR and "除毛" in msgSTR:    # msgSTR = 請問你們只有除毛可以預約嗎
                        replySTR = "是的～但我們其他療程的預約功能在不久後會與你見面！敬請期待！"                    
                    else:
                        replySTR = "我只能回答醫美相關問題喔～請重新輸入你的需求～\n可以跟我說「我想除毛」或是「我想預約星期一下午ＯＯＯ醫師的除毛門診」喔！"
                        mscDICT[client.user.id] = {"bodypart": None,
                                                   "request": "",
                                                   "confirm": "",
                                                   "queryIntentSTR": "",
                                                   "bodyQuestionSTR": "",
                                                   "appointmentQuestionSTR": "",
                                                   "appointmentClinic": "",
                                                   "appointmentDoctor": "",
                                                   "appointmentDay": "",
                                                   "appointmentTime": "",
                                                   "medicalHistory": "",
                                                   "updatetime": datetime.now(),
                                                   "finish": ""
                                                   }             
                
        else:       
            replySTR = "我只能回答醫美相關問題喔～有沒有相關問題想問我呀？\n可以跟我說「我想除毛」或是「我想預約星期一下午ＯＯＯ醫師的除毛門診」喔！"
            mscDICT[client.user.id] = {"bodypart": None,
                                       "request": "",
                                       "confirm": "",
                                       "queryIntentSTR": "",
                                       "bodyQuestionSTR": "",
                                       "appointmentQuestionSTR": "",
                                       "appointmentClinic": "",
                                       "appointmentDoctor": "",
                                       "appointmentDay": "",
                                       "appointmentTime": "",
                                       "medicalHistory": "",
                                       "updatetime": datetime.now(),
                                       "finish": ""
                                       }         
                                 
    except Exception as e:
        logging.error("[MSG response ERROR] {}".format(str(e)))

    pprint(mscDICT)
    
    if replySTR:    # 回應 User 訊息
        await message.reply(replySTR)
    return


if __name__ == "__main__":
    client.run(accountDICT["discord_token"])
    