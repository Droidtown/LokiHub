#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import json
from ArticutAPI import Articut
from decimal import Decimal, ROUND_HALF_UP

app = Flask(__name__)

# line bot info
with open("line_bot.json", encoding="utf-8") as f:
    linebotDICT = json.loads(f.read())
line_bot_api = LineBotApi(linebotDICT["line_bot_api"])
handler = WebhookHandler(linebotDICT["handler"])
# articut info
with open("account.json", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())
articut = Articut(username=accountDICT["username"], apikey=accountDICT["apikey"])
# 代名詞 
with open("Dict/pronoun.json", encoding="utf-8") as f:
    pronounDICT = json.loads(f.read())
# 絕對性詞彙 
with open("Dict/absolution.json", encoding="utf-8") as f:
    absolutionDICT = json.loads(f.read())    
# 負向詞彙
with open("Dict/negative.json", encoding="utf-8") as f:
    negativeDICT = json.loads(f.read())
# 正向詞彙
with open("Dict/positive.json", encoding="utf-8") as f:
    positiveDICT = json.loads(f.read())
# 其他代名詞詞彙
with open("Dict/other_pronoun.json", encoding="utf-8") as f:
    otherpronounDICT = json.loads(f.read())

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 忽略的詞性
ignorance = ["FUNC_conjunction", "FUNC_degreeHead", "FUNC_determiner", "FUNC_inner", "FUNC_inter", "FUNC_modifierHead", "FUNC_negation", "ASPECT"]
# 憂鬱指數
index = 0

def wordExtractor(inputLIST, unify=True):
    '''
    配合 Articut() 的 .getNounStemLIST() 和 .getVerbStemLIST() …等功能，拋棄位置資訊，只抽出詞彙。
    '''
    resultLIST = []
    for i in inputLIST:
        if i == []:
            pass
        else:
            for e in i:
                resultLIST.append(e[-1])
    if unify == True:
        return sorted(list(set(resultLIST)))
    else:
        return sorted(resultLIST)

def MakePronoun(inputLIST, inputDICT):
    global index
    index = 0
    first_person = 0
    others = 0
    dictLen = 0
    for i in inputLIST:
        if i in pronounDICT["first"]:
            first_person += 1
        #else:
            #others += 1
            
    inputDICT = inputDICT["result_obj"]       
    for i in range(len(inputDICT)):
        for j in range(len(inputDICT[i])):
            if inputDICT[i][j]["pos"] not in ignorance:
                dictLen += 1                  
            #if inputDICT[i][j]["text"] in otherpronounDICT["others"]:
                #others += 1 
                
    msg = "[代名詞 使用情況]\n"  
    msg += ("第一人稱：" + str(first_person) + '\n')
    #msg += ("其他人稱：" + str(others) + '\n')
    if first_person > 1:
        msg += ("第一人稱占比：" + str(Decimal(str((first_person/dictLen)*100)).quantize(Decimal('.00'), ROUND_HALF_UP)) + "%\n")
    else:
        first_person = 1
        msg += ("第一人稱占比：" + str(Decimal(str((first_person/dictLen)*100)).quantize(Decimal('.00'), ROUND_HALF_UP)) + "%\n")
    index += Decimal(str((first_person/dictLen)*25)).quantize(Decimal('.00'), ROUND_HALF_UP)
    return msg

def MakeAbsolution(inputDICT):
    global index
    absolute = 0
    dictLen = 0
    inputDICT = inputDICT["result_obj"]
    for i in range(len(inputDICT)):
        for j in range(len(inputDICT[i])): 
            if inputDICT[i][j]["pos"] not in ignorance:
                dictLen += 1
            if inputDICT[i][j]["text"] in absolutionDICT["absolution"]:
                absolute += 1
    
    msg = "\n[絕對性詞彙 使用情況]\n"
    msg += ("絕對性詞彙：" + str(absolute) + '\n')
    msg += ("絕對性詞彙占比：" + str(Decimal(str((absolute/dictLen)*100)).quantize(Decimal('.00'), ROUND_HALF_UP))+ "%\n")
    index += Decimal(str((absolute/dictLen)*54)).quantize(Decimal('.00'), ROUND_HALF_UP)
    return msg    

def MakeDepression(inputDICT):
    global index
    depress = 0
    encourage = 0
    dictLen = 0
    inputDICT = inputDICT["result_obj"]
    for i in range(len(inputDICT)):
        for j in range(len(inputDICT[i])):
            if inputDICT[i][j]["pos"] not in ignorance:
                dictLen += 1
            if inputDICT[i][j]["text"] in negativeDICT["negative"]:
                depress += 1
            elif inputDICT[i][j]["text"] in negativeDICT["death"]:
                depress += 2
            elif inputDICT[i][j]["text"] in negativeDICT["medicine"]:
                depress += 2
            elif inputDICT[i][j]["text"] in negativeDICT["disease"]:
                depress += 2                
            #elif inputDICT[i][j]["text"] in positiveDICT["positive"]:
                #encourage += 1
    
    msg = "\n[負向詞彙 使用情況]\n"
    msg += ("負向詞彙：" + str(depress) + '\n')
    #msg += ("正向詞彙：" + str(encourage) + '\n')
    msg += ("負向詞彙占比：" + str(Decimal(str((depress/dictLen)*100)).quantize(Decimal('.00'), ROUND_HALF_UP))+ "%\n")
    #msg += ("正向詞彙占比：" + str(Decimal(str((encourage/dictLen)*100)).quantize(Decimal('.00'), ROUND_HALF_UP))+ "%")
    index += Decimal(str((depress/dictLen)*21)).quantize(Decimal('.00'), ROUND_HALF_UP)
    return msg

def MakeIndex():
    global index
    msg = "\n[憂鬱文本分析]\n"
    msg += ("憂鬱指數：" + str(index) + '\n')
    msg += ("提醒您：此工具的用途為分析有潛在憂鬱傾向的文本。若您的文本之憂鬱指數高於5.5，代表此文本與其他憂鬱文本的相似度較高。")
    return msg

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    inputSTR = event.message.text
    # input userDefinedDict
    mixedDICT = {**absolutionDICT, **negativeDICT, **positiveDICT, **otherpronounDICT}
    with open("mixedDICT.json", mode="w", encoding="utf-8") as f:
        json.dump(mixedDICT, f, ensure_ascii=False)
    # parse with userDefinedDict
    inputDICT = articut.parse(inputSTR, userDefinedDictFILE="./mixedDICT.json")
    inputLIST = articut.getPersonLIST(inputDICT)
    inputLIST = wordExtractor(inputLIST, unify=False)    
    PronounMsg = MakePronoun(inputLIST, inputDICT)
    AbsolutionMsg = MakeAbsolution(inputDICT)
    DepressionMsg = MakeDepression(inputDICT)
    IndexMsg = MakeIndex()
    ResultMsg = PronounMsg + AbsolutionMsg + DepressionMsg + IndexMsg
    SendMsg=[TextSendMessage(text=ResultMsg)]
    line_bot_api.reply_message(event.reply_token, SendMsg)    
    
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
