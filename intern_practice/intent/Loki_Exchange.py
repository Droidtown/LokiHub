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

#creat a dictionary first
moneyDICT = {'台幣': 'TWD','新台幣':'TWD','美元':'USD','鎂':'USD', '美金': 'USD', '歐元': 'EUR', '日圓': 'JPY', '英鎊': 'GBP', '瑞士法郎': 'CHF', '加幣': 'CAD', '澳幣': 'AUD', '巴西黑奧': 'BRL', '人民幣': 'CNY', '捷克克朗': 'CZK', '丹麥克羅納': 'DKK', '港幣': 'HKD', '匈牙利': 'HUF', '印尼盧比': 'IDR', '印度盧比': 'INR', '韓圜': 'KRW', '墨西哥披索': 'MXN', '挪威克?': 'NOK', '紐幣': 'NZD', '菲律賓披索': 'PHP', '波蘭茲羅提': 'PLN', '俄國盧布': 'RUB', '瑞典克郎': 'SEK', '新加坡幣': 'SGD', '泰銖': 'THB', '土耳其里拉': 'TRL', '南非幣': 'ZAR', '馬來西亞': 'MYR', '斯洛伐克克朗': 'SKK', '沙烏地阿拉伯利雅': 'SAR', '哥倫比亞披索': 'COP', '辛巴威': 'ZWD', '摩洛哥迪拉姆': 'MAD', '埃及鎊': 'EGP', '以色列謝克': 'ILS', '智利披索': 'CLP', '阿根廷披索': 'ARS', '玻利維亞幣': 'BOB', '厄爪多爾蘇克雷': 'ECS', '巴拿馬巴布亞': 'PAB', '委內瑞拉銀幣': 'VEB', '巴基斯坦盧比': 'PKR', '斯里蘭卡盧比': 'LKR', '哥斯大黎加': 'CRC', '新土耳其里拉': 'TRY', '肯亞先令': 'KES', '模里西斯盧比': 'MUR', '越南幣': 'VND', '冰島幣': 'ISK', '阿拉伯聯合大公國迪拉姆': 'AED', '秘魯索爾': 'PEN', '黃金': 'XAU', '境外人民幣': 'CNH', '科威特幣': 'KWD', '澳門幣': 'MOP'}


currencyLIST = []
for x in moneyDICT:
    currencyLIST.append(x)
    currencyLIST.extend(moneyDICT[x])
        
def GetCurrency(inputSTR):
    for currency in currencyLIST:
        if currency in inputSTR:
            return currency        
    
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Exchange:
            print("[Exchange] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
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
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100元][美金]要多少[台幣]":
        # write your code here
        resultDICT["src"]=args[1]
        resultDICT["tgt"]=args[2]
        resultDICT["amt"]=args[0]        
        pass

    if utterance == "[100台幣]換[美金]":
        # write your code here
        resultDICT["src"]=GetCurrency(args[0])
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]=args[0]    
        pass

    if utterance == "[100美金]能換多少[台幣]":
        # write your code here
        resultDICT["src"]=GetCurrency(args[0])
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]=args[0]      
        pass
#如果是文字的一百美金感覺會比較複雜
    if utterance == "[100美金]要[台幣]多少":
        # write your code here
        resultDICT["src"]=GetCurrency(args[0])
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]=args[0]       
        pass

    if utterance == "[100美金]要多少[台幣]":
        # write your code here
        resultDICT["src"]=GetCurrency(args[0])
        resultDICT["tgt"]=args[1]
        resultDICT["amt"]=args[0]       
        pass

    if utterance == "[今天][美金]兌換[台幣]是多少":
        # write your code here
        resultDICT["src"]= args[1]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= "1"        
        pass

    if utterance == "[我]想要換[100元][美金]":
        # write your code here
        #當有缺漏的時候你可以把那個設成default接著在function中設定為台幣
        #你也可以設成 if arg in ["我"]: 來限制你想要的對象
        resultDICT["src"]= "台幣"
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]    
        pass

    if utterance == "[我]想要[美金][100元]":
        # write your code here
        resultDICT["src"]= "台幣"
        resultDICT["tgt"]= args[1]
        resultDICT["amt"]=  args[2]           
        pass

    if utterance == "[我]想買[100元][美金]":
        # write your code here
        resultDICT["src"]= "台幣"
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]=  args[1]           
        pass

    if utterance == "[我]想買[美金][100元]":
        # write your code here
        resultDICT["src"]= "台幣"
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]=  args[1]          
        pass

    if utterance == "[美金][100]要[台幣]多少":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]
        pass

    if utterance == "[美金][100]要多少[台幣]":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]        
        pass

    if utterance == "[美金][100元]可以兌換[台幣]多少":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]        
        pass

    if utterance == "[美金][100元]可以兌換多少[台幣]":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]        
        pass

    if utterance == "[美金][100元]要[台幣]多少":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]        
        pass

    if utterance == "[美金][100元]要多少[台幣]":
        # write your code here
        resultDICT["src"]= args[0]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[1]        
        pass
    
    if utterance == "[100元][台幣]換[美金]":
        resultDICT["src"]= args[1]
        resultDICT["tgt"]= args[2]
        resultDICT["amt"]= args[0]
        pass
    
    if utterance == "[我]想換[200美金]":
        # args [我, 200美金]  
        resultDICT["src"]= re.findall("[^\\d]+",args[1])
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= re.findall("\\d+",args[1])
        pass
    
    if utterance == "[100美金]怎麼換":
        # args [100美金]
        resultDICT["src"]= re.findall("[^\\d]+",args[0])
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= re.findall("\\d+",args[0])
        pass
        
    if utterance == "[我]想兌換[200元][美金]":
        # args [我, 200元, 美金]
        resultDICT["src"]= args[2]
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]
        pass
    
    if utterance == "[我]要兌換[200元][美金]":
        # args [我, 200元, 美金] 
        resultDICT["src"]= args[2]
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]
        pass
    
    if utterance == "[我]可以換一下[200元][美金]":
        # args [我, 200元, 美金] 
        resultDICT["src"]= args[2]
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]
        
    if utterance == "[我]可以換[個][200元][美金]":
        # args [我, 個, 200元, 美金]  
        resultDICT["src"]= args[2]
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]
        pass
        
    if utterance == "[我]想要換一下[100元][美金]":
        # args [我, 100元, 美金]
        resultDICT["src"]= args[2] 
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]           
        pass
    
    if utterance == "[我]想要換[個][100元][美金]":
        # args [我, 個, 100元, 美金]
        resultDICT["src"]= args[3] 
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[2]           
        pass
        
    if utterance == "[我]想要[100][鎂]":
         # args [我, 100, 鎂]
        resultDICT["src"]= args[2] 
        resultDICT["tgt"]= "台幣"
        resultDICT["amt"]= args[1]           
        pass
        
    return resultDICT

