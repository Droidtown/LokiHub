#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from word2number.w2n import word_to_num as w2n

def numExtractor(inputSTR):
    '''
    extract number from inputSTR and return it as Int. or Float.
    '''
    #ToDo: Need to consider "105 dollars and forty cents"
    if isinstance(inputSTR, int) or isinstance(inputSTR, float):
        return inputSTR
    else:
        pass
    inputSTR = inputSTR.replace(",", "").replace("'", "").replace("$", "")
    numberWordLIST = []
    for i in inputSTR.split(" "):
        try:
            float(i[0])
            return w2n(i)
        except:
            try:
                w2n(i)
                numberWordLIST.append(i)
            except:
                if i in ("and", "point"):
                    numberWordLIST.append(i)
                else:
                    pass
    try:
        number = w2n(" ".join(numberWordLIST))
        return number
    except:
        return None

if __name__ == "__main__":
    inputSTR = "5 prides of"
    print(numExtractor(inputSTR))