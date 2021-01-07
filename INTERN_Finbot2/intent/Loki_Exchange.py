#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Exchange
    
    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict
    
    Output:
        resultDICT    dict
"""

DEBUG_Exchange = True
userDefinedDICT = {}
import re
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
        print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[100元][台幣]換[美金]":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100元][美金]可以兌換[台幣]多少":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100元][美金]可以兌換多少[台幣]":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100元][美金]要[台幣]多少":
        # write your code here
        pass

    if utterance == "[100元][美金]要多少[台幣]":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100台幣]換[美金]":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[0])))
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[0])))       
        pass

    if utterance == "[100美金]怎麼換":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[0])))
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[0])))      
        pass

    if utterance == "[100美金]能換多少[台幣]":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[0])))
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[0])))       
        pass

    if utterance == "[100美金]要[台幣]多少":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[0])))
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[0])))         
        pass

    if utterance == "[100美金]要多少[台幣]":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[0])))
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[0])))         
        pass

    if utterance == "[今天][美金]兌換[台幣]是多少":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]= "1"      
        pass

    if utterance == "[我]可以換[個][200元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=args[2]          
        pass

    if utterance == "[我]可以換一下[200元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]  
        pass

    if utterance == "[我]想兌換[200元][美金]":
        # write your code here
        resultDICT["src"]=args[2]
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]=args[1]  
        pass

    if utterance == "[我]想換[200美金]":
        # write your code here
        resultDICT["src"]="".join(map(str,re.findall("[^\\d]+", args[1])))
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]="".join(map(str,re.findall("[\\d]+", args[1])))        
        pass

    if utterance == "[我]想要[100][鎂]":
        # write your code here
        resultDICT["src"]=args[2]
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]=args[1]        
        pass

    if utterance == "[我]想要[100元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]          
        pass

    if utterance == "[我]想要[美金][100元]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]=args[2]          
        pass

    if utterance == "[我]想要換[個][100元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[3]
        resultDICT["amt"]=args[2]          
        pass

    if utterance == "[我]想要換一下[100元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]          
        pass

    if utterance == "[我]想買[100元][美金]":
        # write your code here
        resultDICT["src"]=args[2]
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]=args[1]          
        pass

    if utterance == "[我]想買[美金][100元]":
        # write your code here
        resultDICT["src"]=args[2]
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]=args[1]       
        pass

    if utterance == "[我]要兌換[200元][美金]":
        # write your code here
        resultDICT["src"]="台幣"
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]          
        pass

    if utterance == "[美金][100]要[台幣]多少":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]          
        pass

    if utterance == "[美金][100]要多少[台幣]":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass

    if utterance == "[美金][100元]可以兌換[台幣]多少":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass

    if utterance == "[美金][100元]可以兌換多少[台幣]":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass

    if utterance == "[美金][100元]要[台幣]多少":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass

    if utterance == "[美金][100元]要多少[台幣]":
        # write your code here
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass
    if utterance == "[美金][100元]是多少[法郎]":
         # args [美金, 100元, 法郎] 
        resultDICT["src"]=args[0]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[1]         
        pass        
    if utterance == "給[我][100美金]":
        # args [我, 100美金]
        resultDICT["src"]="".join(map(str, re.findall("[^\\d]+", args[1])))
        resultDICT["tgt"]="台幣"
        resultDICT["amt"]="".join(map(str, re.findall("[\\d]+", args[1]))) 
        pass
    
    return resultDICT