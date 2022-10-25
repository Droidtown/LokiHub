#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for food

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from ArticutAPI import Articut
import cn2num
import json
import os
import re

with open("account.info.json", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(username = accountDICT["username"], apikey = accountDICT["api_key"])

DEBUG_food = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_infoBMR":["生理性別","性別","體重","身高","年齡"],"_asSports":["上樓梯","下樓梯","丟飛盤","健走","划獨木舟","划船","划船比賽","快走","快跑","慢走","慢跑","拳擊","攀岩","游泳","溜冰刀","溜直排輪","溜輪鞋","滑雪","爬山","爬岩","登山","走路","跑步","跳繩","跳舞","騎馬"],"_foodName":["原味蛋餅","火腿蛋餅","九層塔蛋餅","起司蛋餅","培根蛋餅","熱狗蛋餅","蔬菜蛋餅","滿福蛋餅","鮪魚蛋餅","里肌蛋餅","飯糰","紫米飯糰","燒餅","油條","燒餅油條","韭菜盒子","堡","漢堡","華堡","辣味華堡","辣味小華堡","三層華堡","三層犇牛肉堡","總匯辣雞腿堡","吉士火烤牛肉堡","華鱈魚堡","大麥克","麥香魚","吉事漢堡","培根起司蛋堡","雞腿堡","滿福堡","滿福蛋堡","火腿蛋堡","青蔬滿福堡","豬肉滿福堡","豬肉滿福堡加蛋","鮮蔬火腿蛋堡","香雞蛋堡","鮪魚蛋堡","煙燻雞肉蛋堡","花枝蛋堡","咔啦雞腿堡","花生熔岩咔啦雞腿堡","金薯黑爵士咔啦雞腿堡","紐奧良烙烤雞腿堡","玉米咕咕雞漢堡","里肌豬排蛋堡","鮮蝦蛋堡","照燒豬肉蛋堡","總匯漢堡","板烤雞腿堡","嫩煎鷄腿堡","勁辣鷄腿堡","安格斯黑牛堡","蕈菇安格斯黑牛堡","脆皮雞排蛋堡","藍帶起司豬排蛋堡","超厚牛肉起司蛋堡","四盎司牛肉堡","雙層四盎司牛肉堡","雙層牛肉吉士堡","麥克雙牛堡","香烤雞肉堡","勁辣雞腿堡","燒烤牛肉堡","薑燒豬肉長堡","火腿堡","炸雞堡","火雞胸肉堡","義大利經典堡","鮪魚堡","蔬菜堡","火雞火腿堡","花生安格斯牛肉堡","小怪獸香豬脆雞堡","重磅培根雙層辣雞腿堡","重磅培根雙層牛肉堡","安格斯厚切牛肉堡","金沙安格斯牛肉堡","火烤雞腿培根堡","雪藏起司火雞堡","摩斯漢堡","雙層摩斯漢堡","摩斯吉士漢堡","雙層摩斯吉士漢堡","摩斯豬排堡","蜜汁烤雞堡","摩斯鱈魚堡","黃金海老堡","摩斯熱狗堡","摘鮮綠黃金海老堡","薑燒珍珠堡","燒肉珍珠堡","海洋珍珠堡","杏鮑菇珍珠堡","咖哩豬排堡","塔塔鱈魚堡","火腿歐姆蛋堡","培根雞蛋堡","蕃茄吉士蛋堡","三明治","雞肉三明治","香米蝦三明治","烤煎蛋三明治","火腿蛋三明治","起司蛋三明治","培根蛋三明治","薯餅蛋三明治","鮪魚蛋三明治","里肌蛋三明治","日式豬排三明治","照燒豬肉蛋三明治","脆皮雞排蛋三明治","豬排總匯三明治","海陸總匯三明治","黑胡椒牛肉三明治","草莓吐司","草莓厚片","巧克力吐司","巧克力厚片","奶油吐司","奶油厚片","奶酥吐司","奶酥厚片","花生吐司","花生厚片","鍋貼","小籠包","黑胡椒麵","黑胡椒麵加蛋","蘑菇麵","蘑菇麵加蛋","醬燒沙茶麵加蛋","宮保雞丁麵加蛋","三杯雞丁麵加蛋","麻油雞麵加蛋","鍋燒意麵","醡醬麵","炸醬麵","餛飩麵","榨菜肉絲麵","雞絲麵","豬肉鍋燒麵","炒麵","蝦仁炒麵","羊肉麵","香菇雞麵","涼麵","四物雞湯麵","叉燒麵","牛肉麵","大腸蚵仔麵線","絲瓜蚌麵","和風義大利麵","清炒鯷魚橄欖風乾番茄義大利麵","茄汁雞肉義大利麵","原汁墨魚海鮮義大利麵","野菜鮮蔬義大利麵","義式蒜辣培根麵","奶油培根義大利麵","鮮魚義大利麵","麵","泡麵","饅頭","飯","白飯","糙米飯","紫米飯","粥","香煎排骨","豉椒排骨","鹽酥排骨","糖醋排骨","炸豬排","香滷控肉","蘿蔔燒肉","回鍋肉","黑胡椒肉片","醬爆肉片","蒜泥白肉","叉燒肉","清蒸獅子頭","瓜仔肉","滷雞腿","烤腿排","花雕醉雞","黃燜雞丁","雪菜雞片","成都子雞","小黃魚煲","香炸白帶魚","樹子蒸午仔魚","蔥爆鯽魚","醋溜魚塊","五味魚丁","五味軟絲","炸花枝條","紅蘿蔔炒蛋","蕃茄炒蛋","四色炒蛋","蒸蛋","水波蛋","茶葉蛋","水煮蛋","荷包蛋","炒蛋","香滷豆乾","香滷豆干","小魚豆乾","小魚苦瓜","咖哩洋芋","南瓜蓮子","青椒炒培根","甜椒肉片","炒玉米","高麗培根","雙脆肉片","筊白筍炒肉絲","大白炒蝦米","玉米肉絲","麻婆豆腐","肉羹黃瓜","三色豆","鹹菜豬血","油燜苦瓜","苦瓜肉片","拌三絲","炸豆腐","炒高麗菜","炒花椰菜","炒波菜","海芽炒豆芽","涼拌海帶絲","炒地瓜葉","涼拌青花菜","炒空心菜","炒豌豆夾","炒韭菜花","炒菠菜","炒萵苣","炒白菜","炒青江菜","炒牛蒡絲","炒蘿蔔絲","涼拌藕片","炒筍絲","苜蓿芽沙拉","炒筊白筍","涼拌荸齊","滷蘿蔔","醃製嫩薑","涼拌花椰沙拉","沙拉筍","凱撒辣脆鷄沙拉","義式烤鷄沙拉","雞米花田園沙拉","脆雞沙拉","火烤牛肉沙拉","夏威夷鮮蔬沙拉","雞肉總匯沙拉","鮮蔬沙拉","四季沙拉","玉米杯","皮蛋瘦肉粥","炸雞腿飯","炸排骨飯","棒棒腿飯","滷雞腿飯","雞排蓋飯","東坡肉蓋飯","豬排蓋飯","日式豬排蓋飯","豬肉丼飯","雞肉丼飯","牛肉丼飯","豬柳燴飯","羊肉燴飯","韓式泡菜燴飯","咖哩雞燴飯","沙茶豬肉燴飯","蕃茄蘆筍咖哩飯","菠菜香茄咖哩飯","牛肉咖哩飯","雞肉咖哩飯","蔬菜咖哩","日式咖哩鮮蔬","泰式紅咖哩雞肉飯","海鮮咖哩飯","韓式牛肉拌飯","蔬菜拌飯","時蔬健康套餐","南瓜季節鮮蔬飯","蒜泥白肉特餐","蕃茄燉肉特餐","獅子頭特餐","卡拉雞快餐","雞絲飯","滷肉飯","控肉飯","豬腳飯","豬排飯","牛肉飯","滷排骨飯","白燒雞飯","無骨雞排飯","醬燒豬肉飯","沙茶豬肉飯","法式香草雞腿飯","和風燒肉飯","蔬菜培根燉飯","精選野菇乳酪燉飯","薑汁照燒豬肉飯","東坡肉便當","香烤秋刀魚便當","雞肉便當","鴨肉便當","吮指雞腿便當","虱目魚粥","辣炒年糕","昆布湯鍋","味噌湯鍋","薯條","大薯","中薯","小薯","金黃薯","地瓜薯條","甜甜包","蛋撻","蘋果派","洋蔥圈","呱呱包","辣薯球","北海道可麗餅","勁濃起司薯","芝心乳酪棒","青蔬雞柳棒","炸雞腿","原味雞腿","黃金炸雞腿","黃金炸雞排","和風炸雞","和風雞排","哈燒烤腿","摩斯雞塊","原味雞塊","辣味雞塊","黃金雞塊","上校雞塊","阿勇雞塊","辣味雞翅","酥嫩鷄翅","麥脆鷄翅","勁辣香鷄翅","椒麻一口翅","脆皮雞柳條","勁爆雞米花","上校薄皮嫩雞","美式半雞","雞脖子","原味小腿","法蘭克熱狗","綜合堅果包","冰炫風","蛋捲冰淇淋","大蛋捲冰淇淋","德式香腸捲","墨西哥莎莎霸王捲","巴黎卡菲嫩雞捲","墨西哥百匯嫩雞烤餅","草莓乳酪餅","巧克力乳酪餅","奶油乳酪餅","奶酥乳酪餅","花生乳酪餅","起司高鈣乳酪餅","火腿高鈣乳酪餅","培根高鈣乳酪餅","滿福高鈣乳酪餅","熱狗高鈣乳酪餅","原味抓餅","蔥抓餅","蔥蛋抓餅","起司蛋抓餅","培根蛋抓餅","火腿蛋抓餅","蔬菜蛋抓餅","滿福蛋抓餅","里肌蛋抓餅","鬆餅","豬肉鬆餅","鮪魚鬆餅","鮮奶油鬆餅","蜂蜜鬆餅","花生鬆餅","草莓鬆餅","冰淇淋鬆餅","巧克力鬆餅","麵包","波蘿麵包","紅豆麵包","奶酥麵包","全麥核桃麵包","草莓麵包","香蒜麵包","椰子麵包","吐司","小餐包","貝果","起司貝果","乳酪貝果","海鮮披薩","總匯披薩","夏威夷披薩","素食披薩","燻雞披薩","小熱狗","煎餃","水煎包","蘿蔔糕","薯餅","麥香雞","麥脆鷄","麥克雞塊","脆皮雞排","咔啦脆雞","卡拉雞捲","起司豬排","紐奧良半雞","紐奧良手扒雞","義式香草紙包雞","煙燻雞肉捲","生菜熱狗","水餃","奶茶","可樂","紅茶","無糖茶","枸杞茶","菊花茶","洛神花茶","蜂蜜茶","茉香綠茶","多多綠茶","百香綠茶","葡萄柚綠茶","鮮奶茶","茉香奶茶","珍珠奶茶","鮮奶綠","蜂蜜檸檬茶","蜂蜜柚子茶","梅子綠茶","美式咖啡","義式濃縮咖啡","熱咖啡","冰咖啡","熱卡布奇諾","熱拿鐵","冰拿鐵","冰淇淋咖啡","冰摩卡巧克力","冰義式香濃可可","熱義式香濃可可","義式摩卡巧克力","紅茶雪泥","抹茶牛奶","可可牛奶","雪碧","抹茶冰淇淋","香草冰淇淋","豆漿","鹹豆漿","柳橙汁","蘋果多多","貢丸湯","餛飩湯","玉米湯","玉米濃湯","酸辣湯","紅燒湯","水果袋","酪梨","棗子","香蕉","柿子","荔枝","龍眼","火龍果","蘋果","櫻桃","葡萄","鳳梨","柚子","李子","檸檬","芒果","哈密瓜","草莓","西瓜","木瓜","香瓜","水梨","水蜜桃"],"_asMaleFemale":["男","男生","男性","男人","男子","帥哥","大叔","先生","歐巴","女","女生","女人","女性","女子","美女","小姐","阿姨","大嬸"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def loadJson(filename):
    with open(filename,"r") as f:
        result = json.load(f)
    return result

foodDICT  = loadJson("foodDICT.json")

def debugInfo(inputSTR, utterance):
    if DEBUG_food:
        print("[food] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    
    all_calLIST=[]
    amount = 1
    if utterance == "[一碗][白飯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try: 
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        print(args[1])
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
            print("輸入:", args[1], "對應:", foodName)
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
            print("輸入:", args[1], "對應:", foodName)
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal1 = int(amount)*int(cal)
        all_calLIST.append(food_cal1)
        
    
    if utterance == "[一碗][白飯]和[一碗][湯]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[3] in foodDICT.keys():
            cal_2 += foodDICT[args[3]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[3])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[3])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[3]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[3]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0        

        food_cal2 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal2)
        
        #if any(elem is None for elem in [amount_1, cal_1, amount_2, cal_2]) == False:
            #food_cal2 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
            #all_calLIST.append(food_cal2)
        #elif any(elem is None for elem in [amount_1, cal_1]) == True:
            #food_cal2 = int(amount_2)*int(cal_2)
            #all_calLIST.append(food_cal2)
        #elif any(elem is None for elem in [amount_2, cal_2]) == True:
            #food_cal2 = int(amount_1)*int(cal_1)
            #all_calLIST.append(food_cal2)
        #else:
            #food_cal2 = int("0")
            #all_calLIST.append(food_cal2)
    
    if utterance == "[早上]吃了[一碗][白飯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try: 
                    amount = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        if args[2] in foodDICT.keys():
            cal += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal3 = int(amount)*int(cal)
        all_calLIST.append(food_cal3)
    
    if utterance == "[晚餐]還吃了[一碗][白飯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0 
        if args[2] in foodDICT.keys():
            cal += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal4 = int(amount)*int(cal)
        all_calLIST.append(food_cal4)
    
    if utterance == "吃了[一碗][白飯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError:
                    print("index error")
        cal = 0
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal5 = int(amount)*int(cal)
        all_calLIST.append(food_cal5)

    if utterance == "和[一碗][白飯]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal6 = int(amount)*int(cal)
        all_calLIST.append(food_cal6)

    if utterance == "[中午]沒吃":
        food_cal7 = int("0")
        all_calLIST.append(food_cal7)
        
    if utterance == "[早餐]沒吃":
        food_cal8 = int("0")
        all_calLIST.append(food_cal8)
        
    if utterance == "沒吃[晚餐]":
        food_cal9 = int("0")
        all_calLIST.append(food_cal9)
        
    if utterance == "[晚餐]吃[白飯]":
        cal = 0 
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0
        
        food_cal10 = int(cal)
        all_calLIST.append(food_cal10)
        
    if utterance == "[晚餐]是[雞排]":
        cal = 0 
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0
        
        food_cal11 = int(cal)
        all_calLIST.append(food_cal11)
    
    if utterance == "吃[白飯]":
        cal = 0 
        if args[0] in foodDICT.keys():
            cal += foodDICT[args[0]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[0])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[0])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[0]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[0]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal12 = int(cal)
        all_calLIST.append(food_cal12)
        
    if utterance == "和[白飯]":
        cal = 0 
        if args[0] in foodDICT.keys():
            cal += foodDICT[args[0]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[0]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[0]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0
        
        food_cal13 = int(cal)
        all_calLIST.append(food_cal13)
        
    if utterance == "沒吃":
        food_cal14 = int("0")
        all_calLIST.append(food_cal14)
        
    if utterance == "[雞排]和[紅茶]":
        cal_1 = 0
        if args[0] in foodDICT.keys():
            cal_1 += foodDICT[args[0]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[0])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[0])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[0]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[0]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[1] in foodDICT.keys():
            cal_2 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal15 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal15)
                
    if utterance == "吃了[一碗][白飯]和[一碗][湯]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[3] in foodDICT.keys():
            cal_2 += foodDICT[args[3]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[3])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[3])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[3]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[3]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal16 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal16)
        
    if utterance == "[早上]吃了[一碗][白飯]和[一碗][湯]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal17 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal17)
        
    if utterance == "[晚餐]吃了[一碗][白飯]和[一碗][湯]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal18 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal18)
    
    if utterance == "[一片][吐司]加[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[3] in foodDICT.keys():
            cal_2 += foodDICT[args[3]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[3])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[3])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[3]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[3]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal19 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal19)
    
    if utterance == "[一片][吐司]配[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[2]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[2]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[2],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[3] in foodDICT.keys():
            cal_2 += foodDICT[args[3]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[3])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[3])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[3]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[3]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal20 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal20)
        
    if utterance == "[吐司]加[奶茶]":
        cal_1 = 0
        if args[0] in foodDICT.keys():
            cal_1 += foodDICT[args[0]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[0])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[0])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[0]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[0]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[1] in foodDICT.keys():
            cal_2 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal21 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal21)
    
    if utterance == "[吐司]配[奶茶]":
        cal_1 = 0
        if args[0] in foodDICT.keys():
            cal_1 += foodDICT[args[0]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[0])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[0])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[0]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[0]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[1] in foodDICT.keys():
            cal_2 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal22 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal22)

    if utterance == "[早上]吃[一片][吐司]加[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal23 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal23)

    if utterance == "[早上]吃[一片][吐司]配[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal24 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal24)

    if utterance == "[早上]吃[吐司]加[奶茶]":
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[2] in foodDICT.keys():
            cal_2 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal25 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal25)

    if utterance == "[早上]吃[吐司]配[奶茶]":
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[2] in foodDICT.keys():
            cal_2 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal26 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal26)
    
    if utterance == "[早餐]吃[一片][吐司]加[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal27 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal27)
    
    if utterance == "[早餐]吃[一片][吐司]配[一杯][奶茶]":
        amount_1 = 1
        amount_2 = 1
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount_1 = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount_1 = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_1 = 0
        if args[2] in foodDICT.keys():
            cal_1 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0

        for i in num:
            if i in args[3]:
                amount_2 = cn2num.transform(i)
            elif re.search("\d*", args[3]) != None:
                try:
                    amount_2 = str(list(articut.parse(args[3],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal_2 = 0
        if args[4] in foodDICT.keys():
            cal_2 += foodDICT[args[4]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[4])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[4])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[4]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[4]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0

        food_cal28 = int(amount_1)*int(cal_1)+int(amount_2)*int(cal_2)
        all_calLIST.append(food_cal28)

    if utterance == "[早餐]吃[吐司]加[奶茶]":
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[2] in foodDICT.keys():
            cal_2 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal29 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal29)

    if utterance == "[早餐]吃[吐司]配[奶茶]":
        cal_1 = 0
        if args[1] in foodDICT.keys():
            cal_1 += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal_1 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal_1 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_1 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_1 += 0
        
        cal_2 = 0
        if args[2] in foodDICT.keys():
            cal_2 += foodDICT[args[2]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[2])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[2])), None)
            cal_2 += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[2]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[2]), None)
            cal_2 += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal_2 += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal_2 += 0
            
        food_cal30 = int(cal_1)+int(cal_2)
        all_calLIST.append(food_cal30)
    
    if utterance == "加[一杯][奶茶]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal31 = int(amount)*int(cal)
        all_calLIST.append(food_cal31)
    
    if utterance == "配[一杯][奶茶]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        if args[1] in foodDICT.keys():
            cal += foodDICT[args[1]]
        elif next((key for key in foodDICT.keys() if key.endswith(args[1])), None) != None:
            foodName = next((key for key in foodDICT.keys() if key.endswith(args[1])), None)
            cal += foodDICT[foodName]
        elif next((key for key in foodDICT.keys() if key in args[1]), None) != None:
            foodName = next((key for key in foodDICT.keys() if key in args[1]), None)
            cal += foodDICT[foodName]
        else:
            try:
                if next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-1:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-2:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
                elif next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None) != None:
                    foodName = next((key for key in foodDICT.keys() if key in inputSTR[-3:]), None)
                    cal += foodDICT[foodName]
                    print("輸入:", args, "對應:", foodName)
            except:
                cal += 0

        food_cal32 = int(amount)*int(cal)
        all_calLIST.append(food_cal32)
        
    if utterance == "[一盤][義大利][麵]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal33 = int(amount)*int(cal)
        all_calLIST.append(food_cal33)
    
    if utterance == "吃了[一盤][義大利][麵]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[0]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[0]) != None:
                try:
                    amount = str(list(articut.parse(args[0],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal34 = int(amount)*int(cal)
        all_calLIST.append(food_cal34)
    
    if utterance == "[午餐]吃了[一盤][義大利][麵]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal35 = int(amount)*int(cal)
        all_calLIST.append(food_cal35)
    
    if utterance == "[中午]吃了[一盤][義大利][麵]":
        num = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        for i in num:
            if i in args[1]:
                amount = cn2num.transform(i)
            elif re.search("\d*", args[1]) != None:
                try:
                    amount = str(list(articut.parse(args[1],level="lv3")["number"].values())[0])
                except IndexError: 
                    print("index error")
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal36 = int(amount)*int(cal)
        all_calLIST.append(food_cal36)
        
    if utterance == "[中午]吃[義大利][麵]":
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal37 = int(cal)
        all_calLIST.append(food_cal37)
    
    if utterance == "[午餐]吃[義大利][麵]":
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal38 = int(cal)
        all_calLIST.append(food_cal38)
    
    if utterance == "[午餐]是[義大利][麵]":
        cal = 0
        try:
            if next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-4:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-3:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-2:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
            elif next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None) != None:
                foodName = next((key for key in foodDICT.keys() if key.endswith(inputSTR[-1:])), None)
                cal += foodDICT[foodName]
                print("輸入:", args, "對應:", foodName)
        except:
            cal += 0

        food_cal39 = int(cal)
        all_calLIST.append(food_cal39)


    if "food_cal" in resultDICT:
        resultDICT["food_cal"].extend(all_calLIST)
    else:
        resultDICT["food_cal"] = all_calLIST
    return resultDICT