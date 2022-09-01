#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for syntax

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from hashlib import new
import json
import os
from unittest import result

DEBUG_syntax = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_syntax:
        print("[syntax] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[他們][都][從不]同意":
        newSTR = args[0]+args[2]+'同意'
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'never'

    if utterance == "[他們]的[名字]不[常常]利用[太特別]的[字]":
        newSTR = inputSTR.replace('不常常利用','不常用')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'often'

    if utterance == "[夏天]我[爸爸]說":
        newSTR = args[0]+'的時候'+args[1]+'說(+內容)'
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'time'

    if utterance == "[大家][都]希望[會]快[點]得到解決[這個][很嚴重]的問題":
        newSTR = inputSTR.replace('會','能').replace('得到','')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'solution'

    if utterance == "[學生]不[能]來校[內]":
        newSTR = inputSTR.replace('來校內','到校')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'dao'

    if utterance == "[我][只][會]聊天[我]的最愛":
        newSTR = inputSTR.replace('聊天', '聊').replace('最愛','最愛的(+事物)')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'liao'

    if utterance == "[我][可以]解釋[我][生活]的影響":
        newSTR = args[0]+args[1]+inputSTR[3:5]+'對'+args[2]+args[3]+utterance[-3:]
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'explanation'

    if utterance == "[我][生活]被[這個][情況]受到非常不好的影響":
        newSTR = inputSTR.replace(f'{args[0]}',f'{args[0]}的').replace('被','因為')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'result'

    if utterance == "[我]想通過寫信[坦誠地]跟[你們]聊了聊":
        newSTR = inputSTR.replace('聊了聊','聊一聊')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'say'

    if utterance == "[我]跟[我]的[朋友]不[可以]聊天[這本][書]":
        newSTR = inputSTR.replace('聊天','聊')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'liao'

    if utterance == "[我們][下個星期]再會談論[這部][電視劇]":
        if '下' in args[1] or '明' in args[1] or '後' in args[1]:
            newSTR = inputSTR.replace('再會','會再')
        else:
            newSTR = args[0]+args[1]+'談論過'+args[2]+args[3]
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'again'

    if utterance == "[我們]的偶遇[以前]":
        newSTR = '在'+inputSTR
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'before'

    if utterance == "[新冠肺炎][疫情]對[美國][生活]有不少了的影響":
        newSTR = inputSTR.replace('少了','少')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent5'

    if utterance == "[新冠肺炎]給[經濟]影響":
        newSTR = inputSTR.replace('給','帶來')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent6'

    if utterance == "[最近]教育和工作的變化[都]就是[額外]的[壓力]":
        newSTR = inputSTR.replace('就是','都是')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'dou'

    if utterance == "[重要]的[日用品]還不買":
        newSTR = inputSTR.replace('還不買','還買不到')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'sent7'

    if utterance == "新冠肺炎[很高]的傳染[性]":
        newSTR = '新冠肺炎有'+args[0]+'的傳染'+args[1]
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'you'

    if utterance == "新館肺炎的防疫不太成功的":
        newSTR = '新冠肺炎'+utterance[5:7]+'是'+utterance[7:]
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'cleft'

    if utterance == "旅遊在[台灣]":
        newSTR = '在'+args[0]+utterance[:2]
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'loc'

    if utterance == "根據[她]說":
        newSTR = inputSTR.replace('說','說的內容')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'genju'

    if utterance == "每[夏天][他]讓了我[妹妹]和[我]寫書報告":
        newSTR = inputSTR.replace('每','每到').replace('讓了','讓')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'rang'

    if utterance == "沒是[那麼][對抗性]":
        newSTR = '是沒'+args[0]+args[1]+'的'
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'cleft'

    if utterance == "這[導致]了諸如畢業[舞會]、[高年級][學生]慶祝[活動]、[實地]考察旅行等[活動]什麼的被取消":
        newSTR = inputSTR.replace('諸如','').replace('什麼的','都')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'etc'

    if utterance == "還[許多][人]無視[政府]的[新冠肺炎]的[規則]":
        newSTR = inputSTR.replace('還','還有')
        resultDICT['suggestion'] = newSTR
        resultDICT['error'] = 'hai'

    resultDICT['inq'] = None #inq的值為None
    
    return resultDICT