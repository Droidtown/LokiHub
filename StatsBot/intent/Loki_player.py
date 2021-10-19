#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for player

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json

DEBUG_player = True

with open("./intent/nba_teams.json", encoding="utf-8") as f:
    teamDICT = json.loads(f.read())

levelDICT = {'平均':['平均', '場均'], '單場':['單場', '一場']}

stat_index = {'得分': 'pts', '籃板': 'reb', '助攻':'ast', '阻攻':'stl', '抄截':'blk' }


def get_team(resultDICT, args):
    """Get NBA team name"""
    print(args)
    for i in range(len(args)):
        for key in teamDICT.keys():
            if args[i] in teamDICT[key]:
                resultDICT['team'].append(key)
    return resultDICT

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_player:
        print("[player] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT['team'] = []

    if utterance == "[公牛隊][平均][得分]最多是誰":
        resultDICT = get_team(resultDICT, args)
        pass

    if utterance == "[公牛隊][平均][得分]最多的球員":
        resultDICT = get_team(resultDICT, args)
        pass

    if utterance == "[公牛隊][平均][得分]最高是誰":
        resultDICT = get_team(resultDICT, args)
        pass

    if utterance == "[公牛隊][平均][得分]最高的球員":
        resultDICT = get_team(resultDICT, args)
        pass

    return resultDICT