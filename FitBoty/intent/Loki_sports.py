#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for sports

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ArticutAPI import Articut
import json
import os
import re
import cn2num

with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])


DEBUG_sports = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asSports":["丟飛盤","划獨木舟","划船","攀岩","游泳","溜直排輪","滑雪","爬山","登山","走路","跑步","跳繩","跳舞","騎馬"],"_foodName":["三杯雞丁麵加蛋","三色豆","九層塔蛋餅","五味軟絲","五味魚丁","便當","全麥核桃麵包","冰咖啡","冰拿鐵","冰摩卡巧克力","冰淇淋咖啡","冰淇淋鬆餅","冰義式香濃可可","南瓜季節鮮蔬飯","南瓜蓮子","卡拉雞快餐","卡拉雞捲","原味抓餅","原味蛋餅","原汁墨魚海鮮義大利麵","叉燒肉","叉燒麵","可可牛奶","可樂","吐司","吮指雞腿便當","味噌湯鍋","和風燒肉飯","和風義大利麵","咖哩洋芋","咖哩雞燴飯","四物雞湯麵","四色炒蛋","回鍋肉","培根蛋三明治","培根蛋抓餅","培根蛋餅","培根起司蛋堡","培根高鈣乳酪餅","夏威夷披薩","多多綠茶","大白炒蝦米","大腸蚵仔麵線","奶油乳酪餅","奶油厚片","奶油吐司","奶油培根義大利麵","奶茶","奶酥乳酪餅","奶酥厚片","奶酥吐司","奶酥麵包","宮保雞丁麵加蛋","小熱狗","小籠包","小餐包","小魚苦瓜","小魚豆乾","小黃魚煲","巧克力乳酪餅","巧克力厚片","巧克力吐司","巧克力鬆餅","成都子雞","抹茶冰淇淋","抹茶牛奶","拌三絲","控肉飯","日式咖哩鮮蔬","日式豬排蓋飯","昆布湯鍋","時蔬健康套餐","東坡肉便當","東坡肉蓋飯","枸杞茶","柳橙汁","梅子綠茶","棒棒腿飯","椰子麵包","榨菜肉絲麵","樹子蒸午仔魚","水餃","沙拉筍","沙茶豬肉燴飯","沙茶豬肉飯","油燜苦瓜","法式香草雞腿飯","波蘿麵包","泰式紅咖哩雞肉飯","洛神花茶","海芽炒豆芽","海陸總匯三明治","海鮮咖哩飯","海鮮披薩","涼拌海帶絲","涼拌花椰沙拉","涼拌荸齊","涼拌藕片","涼拌青花菜","涼麵","清炒鯷魚橄欖風乾番茄義大利麵","清蒸獅子頭","滷排骨飯","滷肉飯","滷蘿蔔","滷雞腿","滷雞腿飯","滿福蛋堡","滿福蛋抓餅","滿福蛋餅","滿福高鈣乳酪餅","火腿堡","火腿蛋三明治","火腿蛋抓餅","火腿蛋餅","火腿高鈣乳酪餅","火雞火腿堡","火雞胸肉堡","炒地瓜葉","炒波菜","炒牛蒡絲","炒玉米","炒白菜","炒空心菜","炒筊白筍","炒筍絲","炒花椰菜","炒菠菜","炒萵苣","炒蘿蔔絲","炒豌豆夾","炒青江菜","炒韭菜花","炒高麗菜","炸排骨飯","炸花枝條","炸豆腐","炸豬排","炸醬麵","炸雞腿","炸雞腿飯","烤煎蛋三明治","烤腿排","無糖茶","無骨雞排飯","煎餃","煙燻雞肉捲","煙燻雞肉蛋堡","照燒豬肉蛋三明治","照燒豬肉蛋堡","熱卡布奇諾","熱咖啡","熱拿鐵","熱狗蛋餅","熱狗高鈣乳酪餅","熱義式香濃可可","燒烤牛肉堡","燻雞披薩","牛肉丼飯","牛肉咖哩飯","牛肉飯","牛肉麵","獅子頭特餐","玉米濃湯","玉米肉絲","珍珠奶茶","瓜仔肉","甜椒肉片","生菜熱狗","白燒雞飯","白飯","百香綠茶","皮蛋瘦肉粥","筊白筍炒肉絲","粥","精選野菇乳酪燉飯","糖醋排骨","紅燒湯","紅茶","紅蘿蔔炒蛋","紅豆麵包","素食披薩","紫米飯糰","絲瓜蚌麵","總匯披薩","總匯漢堡","羊肉燴飯","羊肉麵","美式咖啡","義大利經典堡","義式摩卡巧克力","義式濃縮咖啡","義式蒜辣培根麵","肉羹黃瓜","脆皮雞排","脆皮雞排蛋三明治","脆皮雞排蛋堡","花枝蛋堡","花生乳酪餅","花生厚片","花生吐司","花生鬆餅","花雕醉雞","苜蓿芽沙拉","苦瓜肉片","茄汁雞肉義大利麵","茉香奶茶","茉香綠茶","草莓乳酪餅","草莓厚片","草莓吐司","草莓鬆餅","草莓麵包","菊花茶","菠菜香茄咖哩飯","葡萄柚綠茶","蒜泥白肉","蒜泥白肉特餐","蒸蛋","蔥爆鯽魚","蔥蛋抓餅","蔬菜咖哩","蔬菜培根燉飯","蔬菜堡","蔬菜拌飯","蔬菜蛋抓餅","蔬菜蛋餅","蕃茄炒蛋","蕃茄燉肉特餐","蕃茄蘆筍咖哩飯","薑汁照燒豬肉飯","薯條","薯餅","薯餅蛋三明治","藍帶起司豬排蛋堡","蘋果多多","蘑菇麵","蘑菇麵加蛋","蘿蔔燒肉","蘿蔔糕","虱目魚粥","蜂蜜柚子茶","蜂蜜檸檬茶","蜂蜜茶","蜂蜜鬆餅","蝦仁炒麵","豆漿","豉椒排骨","豬排總匯三明治","豬排蓋飯","豬排飯","豬柳燴飯","豬肉丼飯","豬肉鍋燒麵","豬腳飯","貝果","貢丸湯","起司蛋三明治","起司蛋抓餅","起司蛋餅","起司豬排","起司貝果","起司高鈣乳酪餅","超厚牛肉起司蛋堡","辣炒年糕","酸辣湯","醃製嫩薑","醋溜魚塊","醡醬麵","醬燒沙茶麵加蛋","醬燒豬肉飯","醬爆肉片","里肌蛋三明治","里肌蛋抓餅","里肌蛋餅","里肌豬排蛋堡","野菜鮮蔬義大利麵","鍋燒意麵","雙脆肉片","雞排蓋飯","雞絲飯","雞絲麵","雞肉丼飯","雞肉便當","雞肉咖哩飯","雞腿堡","雪碧","雪菜雞片","青椒炒培根","韓式泡菜燴飯","韓式牛肉拌飯","餛飩湯","餛飩麵","饅頭","香滷控肉","香滷豆乾","香滷豆干","香炸白帶魚","香烤秋刀魚便當","香烤雞肉堡","香煎排骨","香草冰淇淋","香菇雞麵","香蒜麵包","香雞蛋堡","高麗培根","鮪魚堡","鮪魚蛋三明治","鮪魚蛋堡","鮪魚蛋餅","鮪魚鬆餅","鮮奶油鬆餅","鮮奶綠","鮮奶茶","鮮蝦蛋堡","鮮魚義大利麵","鴨肉便當","鹹菜豬血","鹽酥排骨","麥克雞塊","麵","麻婆豆腐","麻油雞麵加蛋","黃燜雞丁","黑胡椒牛肉三明治","黑胡椒肉片","黑胡椒麵","黑胡椒麵加蛋"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result

sportsDICT  = loadJson("sports_dict.json")
extra_sportsDICT  = loadJson("extra_sports_dict.json")

def debugInfo(inputSTR, utterance):
    if DEBUG_sports:
        print("[sports] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    all_calLIST=[]
    time = 1
    if utterance == "[跳繩][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]        
        
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)
    
    if utterance == "[跳繩][30分鐘]和[重訓][1小時]":
        sports_1 = 0
        if args[0] in sportsDICT.keys():
            sports_1 += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]        
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time_1 = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time_1 = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time_1 = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time_1 = cn2num.transform(args[1])*60 
                
        sports_2 = 0
        if args[2] in sportsDICT.keys():
            sports_2 += sportsDICT[args[2]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[2] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[3]) != None:
            if re.search("\d+分鐘", args[3]) != None:
                time_2 = int(re.search("(\d+)分鐘", args[3]).group(1))
            elif re.search("\d+小時", args[3]) != None:
                time_2 = int(re.search("(\d+)小時", args[3]).group(1))*60  
        else:
            if re.search("分鐘", args[3]) != None:
                time_2 = cn2num.transform(args[3])        
            elif re.search("小時", args[3]) != None:
                time_2 = cn2num.transform(args[3])*60 
                
        sports_cal = float(sports_1)*int(time_1) + float(sports_2)*int(time_2)
        all_calLIST.append(sports_cal)

    if utterance == "[跳繩]和[重訓]各[30分鐘]":
        sports_1 = 0
        if args[0] in sportsDICT.keys():
            sports_1 += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        sports_2 = 0
        if args[1] in sportsDICT.keys():
            sports_2 += sportsDICT[args[1]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[1] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[2]) != None:
            if re.search("\d+分鐘", args[2]) != None:
                time = int(re.search("(\d+)分鐘", args[2]).group(1))
            elif re.search("\d+小時", args[2]) != None:
                time = int(re.search("(\d+)小時", args[2]).group(1))*60  
        else:
            if re.search("分鐘", args[2]) != None:
                time = cn2num.transform(args[2])        
            elif re.search("小時", args[2]) != None:
                time = cn2num.transform(args[2])*60 
        sports_cal = (float(sports_1) + float(sports_2))*int(time)
        all_calLIST.append(sports_cal)

    if utterance == "做[瑜伽][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)

    if utterance == "打[排球][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)

    if utterance == "沒有|無":
        sports_cal = int("0")
        all_calLIST.append(sports_cal)

    if utterance == "沒有運動":
        sports_cal = int("0")
        all_calLIST.append(sports_cal)

    if utterance == "爬[樓梯][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)
        
    if utterance == "跳[國標舞][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)
        
    if utterance == "騎[腳踏車][30分鐘]":
        sports = 0
        if args[0] in sportsDICT.keys():
            sports += sportsDICT[args[0]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[0] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[1]) != None:
            if re.search("\d+分鐘", args[1]) != None:
                time = int(re.search("(\d+)分鐘", args[1]).group(1))
            elif re.search("\d+小時", args[1]) != None:
                time = int(re.search("(\d+)小時", args[1]).group(1))*60  
        else:
            if re.search("分鐘", args[1]) != None:
                time = cn2num.transform(args[1])        
            elif re.search("小時", args[1]) != None:
                time = cn2num.transform(args[1])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)
        
    if utterance == "[30分鐘]的[瑜伽]":
        sports = 0
        if args[1] in sportsDICT.keys():
            sports += sportsDICT[args[1]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[1] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[0]) != None:
            if re.search("\d+分鐘", args[0]) != None:
                time = int(re.search("(\d+)分鐘", args[0]).group(1))
            elif re.search("\d+小時", args[0]) != None:
                time = int(re.search("(\d+)小時", args[0]).group(1))*60  
        else:
            if re.search("分鐘", args[0]) != None:
                time = cn2num.transform(args[0])        
            elif re.search("小時", args[0]) != None:
                time = cn2num.transform(args[0])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)

    if utterance == "[30分鐘]的[瑜伽]和[40分鐘]的[跳繩]":
        sports_1 = 0
        if args[1] in sportsDICT.keys():
            sports_1 += sportsDICT[args[1]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[1] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[0]) != None:
            if re.search("\d+分鐘", args[0]) != None:
                time_1 = int(re.search("(\d+)分鐘", args[0]).group(1))
            elif re.search("\d+小時", args[0]) != None:
                time_1 = int(re.search("(\d+)小時", args[0]).group(1))*60  
        else:
            if re.search("分鐘", args[0]) != None:
                time_1 = cn2num.transform(args[0])        
            elif re.search("小時", args[0]) != None:
                time_1 = cn2num.transform(args[0])*60 
                
        sports_2 = 0
        if args[3] in sportsDICT.keys():
            sports_2 += sportsDICT[args[3]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[3] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[2]) != None:
            if re.search("\d+分鐘", args[2]) != None:
                time_2 = int(re.search("(\d+)分鐘", args[2]).group(1))
            elif re.search("\d+小時", args[2]) != None:
                time_2 = int(re.search("(\d+)小時", args[2]).group(1))*60  
        else:
            if re.search("分鐘", args[2]) != None:
                time_2 = cn2num.transform(args[2])        
            elif re.search("小時", args[2]) != None:
                time_2 = cn2num.transform(args[2])*60 
                
        sports_cal = float(sports_1)*int(time_1) + float(sports_2)*int(time_2)
        all_calLIST.append(sports_cal)
    
    if utterance == "和[40分鐘]的[跳繩]":
        sports = 0
        if args[1] in sportsDICT.keys():
            sports += sportsDICT[args[1]]
        else:
            for key in extra_sportsDICT.keys(): 
                if key in args[1] != None:
                    sports += extra_sportsDICT[key]
        if re.search("\d+", args[0]) != None:
            if re.search("\d+分鐘", args[0]) != None:
                time = int(re.search("(\d+)分鐘", args[0]).group(1))
            elif re.search("\d+小時", args[0]) != None:
                time = int(re.search("(\d+)小時", args[0]).group(1))*60  
        else:
            if re.search("分鐘", args[0]) != None:
                time = cn2num.transform(args[0])        
            elif re.search("小時", args[0]) != None:
                time = cn2num.transform(args[0])*60 
            
        sports_cal = float(sports)*int(time)
        all_calLIST.append(sports_cal)
        
        
    if "sports_cal" in resultDICT:
        resultDICT["sports_cal"].extend(all_calLIST)
    else:
        resultDICT["sports_cal"] = all_calLIST        
    return resultDICT