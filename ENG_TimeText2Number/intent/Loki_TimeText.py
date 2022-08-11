#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for TimeText

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""
import inflect
t2n = inflect.engine()

DEBUG_TimeText = True
userDefinedDICT = {"_timeword":["quarter","o'clock"]}

#using inflect module (https://pypi.org/project/inflect/) to generate clockNumLIST
clockNumDICT = {"zero": 0,
                "zero-one"  : 1,
                "zero-two"  : 2,
                "zero-three": 3,
                "zero-four" : 4,
                "zero-five" : 5,
                "zero-six"  : 6,
                "zero-seven": 7,
                "zero-eight": 8,
                "zero-nine" : 9,
                "zero one"  : 1,
                "zero two"  : 2,
                "zero three": 3,
                "zero four" : 4,
                "zero five" : 5,
                "zero six"  : 6,
                "zero seven": 7,
                "zero eight": 8,
                "zero nine" : 9,
                "one"       : 1,
                "two"       : 2,
                "three"     : 3,
                "four"      : 4,
                "five"      : 5,
                "six"       : 6,
                "seven"     : 7,
                "eight"     : 8,
                "nine"      : 9,
                "ten"       : 10,
                "eleven"    : 11,
                "twelve"    : 12,
                "thirteen"  : 13,
                "fourteen"  : 14,
                "fifteen"   : 15,
                "sixteen"   : 16,
                "seventeen" : 17,
                "eighteen"  : 18,
                "nineteen"  : 19,
                "twenty"    : 20,
                "twenty-one": 21,
                "twenty-two": 22,
                "twenty-three": 23,
                "twenty-four" : 24,
                "twenty-five" : 25,
                "twenty-six"  : 26,
                "twenty-seven": 27,
                "twenty-eight": 28,
                "twenty-nine" : 29,
                "thirty"      : 30,
                "thirty-one"  : 31,
                "thirty-two"  : 32,
                "thirty-three": 33,
                "thirty-four" : 34,
                "thirty-five" : 35,
                "thirty-six"  : 36,
                "thirty-seven": 37,
                "thirty-eight": 38,
                "thirty-nine" : 39,
                "forty"       : 40,
                "forty-one"   : 41,
                "forty-two"   : 42,
                "forty-three" : 43,
                "forty-four"  : 44,
                "forty-five"  : 45,
                "forty-six"   : 46,
                "forty-seven" : 47,
                "forty-eight" : 48,
                "forty-nine"  : 49,
                "fifty"       : 50,
                "fifty-one"   : 51,
                "fifty-two"   : 52,
                "fifty-three" : 53,
                "fifty-four"  : 54,
                "fifty-five"  : 55,
                "fifty-six"   : 56,
                "fifty-seven" : 57,
                "fifty-eight" : 58,
                "fifty-nine"  : 59
            }

# Debug message
def debugInfo(inputSTR, utterance):
    if DEBUG_TimeText:
        print("[TimeText] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[it] be [one]":
        if args[0].lower() == "it":
            if len(args[1].split(" ")) == 1:
                hour = None
                if args[1] in clockNumDICT.keys():
                    if clockNumDICT[args[1]] <= 24:
                        hour = clockNumDICT[args[1]]
                        resultDICT["time"] = "{} is {:02}:00".format(args[0], hour)
            elif len(args[1].split(" ")) <= 3:
                hour = None
                minute = None
                if args[1].split(" ")[0] in clockNumDICT.keys() and " ".join(args[1].split(" ")[1:]) in clockNumDICT.keys():
                    if clockNumDICT[args[1].split(" ")[0]] <= 24 and clockNumDICT[" ".join(args[1].split(" ")[1:])] < 60:
                        hour = clockNumDICT[args[1].split(" ")[0]]
                        minute = clockNumDICT[" ".join(args[1].split(" ")[1:])]
                        resultDICT["time"] = "{:02}:{:02}".format(hour, minute)
            else:
                pass
        else:
            pass

    if utterance == "[it] be [one] o'clock":
        if args[0].lower() == "it":
            if len(args[1].split(" ")) == 1:
                hour = None
                if args[1] in clockNumDICT.keys():
                    if clockNumDICT[args[1]] <= 12:
                        hour = clockNumDICT[args[1]]
                        resultDICT["time"] = "{:02}:00".format(hour)

    if utterance == "[one twenty-seven]":
        #if len(args[0].split(" ")) == 1:                                  #Disabled to prevent a single number under 24 is misinterpretated as time expression.
            #hour = None
            #if args[0] in clockNumDICT.keys():
                #if int(clockNumDICT[args[0]]) <= 24:
                    #hour = clockNumDICT[args[0]]
                    #resultDICT["time"] = "{}:00".format(args[0], hour)
        if 2 <= len(args[0].split(" ")) <= 3:
            hour = None
            minute = None
            if args[0].split(" ")[0] in clockNumDICT.keys() and " ".join(args[0].split(" ")[1:]) in clockNumDICT.keys():
                if clockNumDICT[args[0].split(" ")[0]] <= 24 and clockNumDICT[" ".join(args[0].split(" ")[1:])] < 60:
                    hour = clockNumDICT[args[0].split(" ")[0]]
                    minute = clockNumDICT[" ".join(args[0].split(" ")[1:])]
                    resultDICT["time"] = "{:02}:{:02}".format(hour, minute)
        else:
            pass

    if utterance == "[one] o'clock":
        if len(args[0].split(" ")) == 1:
            hour = None
            if args[0] in clockNumDICT.keys():
                if clockNumDICT[args[0]] <= 12:
                    hour = clockNumDICT[args[0]]
                    resultDICT["time"] = "{:02}:00".format(hour)

    if utterance == "[twenty-four] [to] [two]":
        if args[1] == "to":
            if len(args[2].split(" ")) == 1:
                if args[2] in clockNumDICT.keys():
                    if clockNumDICT[args[2]] == 1:
                        hour = 12
                    elif clockNumDICT[args[2]] <= 12:
                        hour = int(clockNumDICT[args[2]]) - 1
                else:
                    hour = None
            else:
                hour = None

            if len(args[0].split(" ")) == 1:
                if clockNumDICT[args[0]] == 0:
                    minute = "00"
                elif args[0] in clockNumDICT.keys():
                    minute = 60 - clockNumDICT[args[0]]
                else:
                    minute = None
            else:
                minute = None

            if hour != None and minute != None:
                resultDICT["time"] = "{:02}:{:02}".format(hour, minute)


    if utterance == "[twenty-four] minutes [to] [two]":
        if args[1] == "to":
            if len(args[2].split(" ")) == 1:
                if clockNumDICT[args[2]] <= 12:
                    if args[2] in clockNumDICT.keys():
                        if clockNumDICT[args[2]] == 1:
                            hour = 12
                        elif int(clockNumDICT[args[2]]) <= 12:
                            hour = clockNumDICT[args[2]] - 1
                    else:
                        hour = None
                else:
                    hour = None
            else:
                hour = None

            if len(args[0].split(" ")) == 1:
                if clockNumDICT[args[0]] == 0:
                    minute = "00"
                elif args[0] in clockNumDICT.keys():
                    minute = 60 - clockNumDICT[args[0]]
                else:
                    minute = None
            else:
                minute = None

            if hour != None and minute != None:
                resultDICT["time"] = "{:02}:{:02}".format(hour, minute)

    if utterance == "[two] [past] [one]":
        if args[1] == "past":
            if len(args[2].split(" ")) == 1:
                if clockNumDICT[args[2]] <= 24:
                    if args[2] in clockNumDICT.keys():
                        hour = clockNumDICT[args[2]]
                    else:
                        hour = None
                else:
                    hour = None
            else:
                hour = None

            if len(args[0].split(" ")) == 1:
                if clockNumDICT[args[0]] == 0:
                    minute = "00"
                elif args[0] in clockNumDICT.keys():
                    minute = clockNumDICT[args[0]]
                else:
                    minute = None
            else:
                minute = None

            if hour != None and minute != None:
                resultDICT["time"] = "{:02}:{:02}".format(hour, minute)

    if utterance == "[two] minutes [past] [one]":
        if args[1] == "past":
            if len(args[2].split(" ")) == 1:
                if clockNumDICT[args[2]] <= 24:
                    if args[2] in clockNumDICT.keys():
                        hour = clockNumDICT[args[2]]
                    else:
                        hour = None
                else:
                    hour = None
            else:
                hour = None

            if len(args[0].split(" ")) == 1:
                if clockNumDICT[args[0]] == 0:
                    minute = "00"
                elif args[0] in clockNumDICT.keys():
                    minute = clockNumDICT[args[0]]
                else:
                    minute = None
            else:
                minute = None

            if hour != None and minute != None:
                resultDICT["time"] = "{:02}:{:02}".format(hour, minute)

    if utterance == "a quarter [past] [one]":
        if args[0] == "past":
            if len(args[1].split(" ")) == 1:
                if clockNumDICT[args[1]] <= 24:
                    if args[1] in clockNumDICT.keys():
                        hour = clockNumDICT[args[1]]
                    else:
                        hour = None
                else:
                    hour = None
            else:
                hour = None

            if hour != None:
                resultDICT["time"] = "{:02}:15".format(hour)

    if utterance == "a quarter [to] [two]":
        if args[0] == "to":
            if len(args[1].split(" ")) == 1:
                if args[1] in clockNumDICT.keys():
                    if int(clockNumDICT[args[1]]) == 1:
                        hour = 12
                    elif clockNumDICT[args[1]] <= 12:
                        hour = clockNumDICT[args[1]] - 1
                else:
                    hour = None
            else:
                hour = None

            if hour != None:
                resultDICT["time"] = "{:02}:45".format(hour)

    if utterance == "[one-o-two]":
        try:
            if len(args[0].split("-")) == 3:
                argLIST = args[0].split("-")
                if argLIST[1] in ("o", "O", "oh"):
                    if argLIST[0] in clockNumDICT.keys() and argLIST[2] in clockNumDICT.keys():
                        if clockNumDICT[argLIST[0]] <= 24 and clockNumDICT[argLIST[2]] < 10:
                            resultDICT["time"] = "{:02}:{:02}".format(clockNumDICT[argLIST[0]], clockNumDICT[argLIST[2]])
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
        except:
            pass


    if utterance == "quarter [past] [one]":
        if args[0] == "past":
            if len(args[1].split(" ")) == 1:
                if clockNumDICT[args[1]] <= 24:
                    if args[1] in clockNumDICT.keys():
                        hour = clockNumDICT[args[1]]
                    else:
                        hour = None
                else:
                    hour = None
            else:
                hour = None

            if hour != None:
                resultDICT["time"] = "{:02}:15".format(hour)

    if utterance == "quarter [to] [two]":
        if args[0] == "to":
            if len(args[1].split(" ")) == 1:
                if args[1] in clockNumDICT.keys():
                    if clockNumDICT[args[1]] == 1:
                        hour = 12
                    elif clockNumDICT[args[1]] <= 12:
                        hour = clockNumDICT[args[1]] - 1
                else:
                    hour = None
            else:
                hour = None

            if hour != None:
                resultDICT["time"] = "{:02}:45".format(hour)

    return resultDICT