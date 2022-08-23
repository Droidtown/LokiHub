#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import inflect
sp = inflect.engine()

def sgForm(inputSTR):
    inputSTR = inputSTR.lower()
    if inputSTR.endswith("'s"):
        inputSTR = inputSTR.rstrip("'s")
    singularForm = sp.singular_noun(inputSTR)
    if inputSTR.endswith("of"):
        resultSTR = sp.singular_noun(inputSTR.split(" ")[-2])
        if resultSTR == False:
            try:
                resultSTR = inputSTR.split(" ")[0]
            except:
                return inputSTR
    elif inputSTR.startswith("for"):
        resultSTR = sp.singular_noun(inputSTR.split(" ")[-1])
    elif singularForm:
        if " " in singularForm:
            resultSTR = singularForm.split(" ")[-1]
        else:
            resultSTR = singularForm
    else:
        resultSTR = inputSTR
    return resultSTR


def sympyKey(inputSTR):
    inputSTR = inputSTR.strip(" ").replace(" ", "_")
    return inputSTR

if __name__ == "__main__":
    inputSTR = "Numbers"
    print(sgForm(inputSTR))