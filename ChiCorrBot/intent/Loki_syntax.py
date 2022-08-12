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

import json
import os
from ArticutAPI import Articut

with open('./intent/account.info', 'r', encoding='utf-8') as f:
    accountDICT = json.load(f)

articut = Articut(username=accountDICT['username'], apikey=accountDICT['articut_key'])

DEBUG_syntax = True

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
        # write your code here
        pass

    if utterance == "[他們]的[名字]不[常常]利用[太特別]的[字]":
        # write your code here
        pass

    if utterance == "[夏天]我[爸爸]說":
        # write your code here
        pass

    if utterance == "[大家][都]希望[會]快[點]得到解決[這個][很嚴重]的問題":
        # write your code here
        pass

    if utterance == "[學生]不[能]來校[內]":
        # write your code here
        pass

    if utterance == "[我][只][會]聊天[我]的最愛":
        # write your code here
        pass

    if utterance == "[我][可以]解釋[我][生活]的影響":
        # write your code here
        pass

    if utterance == "[我][生活]被[這個][情況]受到非常不好的影響":
        # write your code here
        pass

    if utterance == "[我]想通過寫信[坦誠地]跟[你們]聊了聊":
        # write your code here
        pass

    if utterance == "[我]跟[我]的[朋友]不[可以]聊天[這本][書]":
        # write your code here
        pass

    if utterance == "[我們][下個星期]再會談論[這部][電視劇]":
        # write your code here
        pass

    if utterance == "[我們]的偶遇[以前]":
        # write your code here
        pass

    if utterance == "[新冠肺炎][疫情]對[美國][生活]有不少了的影響":
        # write your code here
        pass

    if utterance == "[新冠肺炎]給[經濟]影響":
        # write your code here
        pass

    if utterance == "[最近]教育和工作的變化[都]就是[額外]的[壓力]":
        # write your code here
        pass

    if utterance == "[重要]的[日用品]還不買":
        # write your code here
        pass

    if utterance == "新冠肺炎[很高]的傳染[性]":
        # write your code here
        pass

    if utterance == "新館肺炎的防疫不太成功的":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentataion'].split('/')
        textSTR = '新冠肺炎'+''.join(textLIST[1:3])+'是'+''.join(textLIST[3:])
        resultDICT['suggestion'] = textSTR
        resultDICT['error'] = 'cleft'

    if utterance == "旅遊在[台灣]":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentation'].split('/')
        textSTR = ''.join(textLIST[1:])+textLIST[0]
        resultDICT['suggestion'] = textSTR
        resultDICT['error'] = 'loc'

    if utterance == "根據[她]說":
        # write your code here
        pass

    if utterance == "每[夏天][他]讓了我[妹妹]和[我]寫書報告":
        # write your code here
        pass

    if utterance == "沒是[那麼][對抗性]":
        # write your code here
        pass

    if utterance == "這[導致]了諸如畢業[舞會]、[高年級][學生]慶祝[活動]、[實地]考察旅行等[活動]什麼的被取消":
        # write your code here
        pass

    if utterance == "還[許多][人]無視[政府]的[新冠肺炎]的[規則]":
        resDICT = articut.parse(inputSTR)
        textLIST = resDICT['result_segmentation'].split('/')
        textSTR = textLIST[0]+'有'+''.join(textLIST[1:])
        resultDICT['suggestion'] = textSTR
        resultDICT['error'] = 'hai'

    return resultDICT