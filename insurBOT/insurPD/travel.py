from insurance_bot import execLoki
from ArticutAPI import Articut
import json
import re


with open(r"account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(accountDICT['username'], accountDICT['api_key'])

with open("answer/reply_insur_travel.json", encoding="utf-8") as f:
    replyDICT = json.load(f)

# 網址
eWeb = replyDICT["e悠遊旅行平安險"]['web']
abroadWeb = replyDICT["180天留遊學差旅專案"]['web']
oneWeb = replyDICT["一日平安專案"]['web']

# 保險
reply_e = replyDICT['e悠遊旅行平安險']['Reply']
reply_180 = replyDICT['180天留遊學差旅專案']['Reply']
reply_ping = replyDICT['一日平安專案']['Reply']

# 回覆
t_reply = replyDICT['travel_reply']

# 支付方式
reply_pay = replyDICT['way_pay']

# 賠償項目
reply_com = replyDICT['compensation']



# test 
def check_place(msgSTR):
    sent = articut.parse(msgSTR)['result_obj'][0]
    place = []
    for check in range(len(sent)):
        if "LOCATION" in sent[check]['pos']:
            place.append(sent[check]['text'])
    return place




def placeCheck(place):
    counties = [
    "基隆",
    "台北",
    "新北",
    "桃園",
    "新竹",
    "苗栗",
    "台中",
    "彰化",
    "南投",
    "雲林",
    "嘉義",
    "台南",
    "高雄",
    "屏東",
    "宜蘭",
    "花蓮",
    "台東",
    "澎湖",
    "金門",
    "連江"
]
    if (place == "台灣" or place == "國內" or place in counties):
        return "國內"
    else:
        return "國外"


def periodCheck(period):
    if articut.parse(period)['result_obj'][0][0]['pos'] == "TIME_year":
        num = re.findall(r'(.)年', period)[0]
        if num.isalpha():
            return int(articut.parse(num, level="lv3")["number"][num]) * 365
        else:
            return int(num) * 365
        
    elif articut.parse(period)['result_obj'][0][0]['pos'] == "TIME_month":
        num = re.findall(r'(.)個月', period)[0]
        if num.isalpha():
            return int(articut.parse(num, level="lv3")["number"][num]) * 30
        else:
            return int(num) * 30
        
    elif articut.parse(period)['result_obj'][0][0]['pos'] == "TIME_day":

        day_pattern = ["(.)天", "(.)日"]
        for d in day_pattern:
            if re.findall(d, period):
                num = re.findall(d, period)[0]
                break

        if num.isalpha():
            return int(articut.parse(num, level="lv3")["number"][num])
        else:
            return int(num)
        
    elif articut.parse(period)['result_obj'][0][0]['pos'] == "TIME_week":

        week_pattern = ["(.)星期", "(.)個禮拜", "(.)個星期", "(.)週", "(.)禮拜"]
        for w in week_pattern:
            if re.findall(w, period):
                num = re.findall(w, period)[0]
                break

        if num.isalpha():
            return int(articut.parse(num, level="lv3")["number"][num]) * 7
        else:
            return int(num) * 7

        
def age_filter(age):
    age = int(age)
    travel_insur = []
    if age < 7 or age >= 18:
        travel_insur.append('e悠遊旅行平安險')
    if 18 <= age <= 74:
        travel_insur.append('180天留遊學差旅專案')
    if age >= 18:
        travel_insur.append('一日平安專案')
    return travel_insur


def res_insurance(age, period, place):
    period = periodCheck(period)
    place = placeCheck(place)
    travel_insur = age_filter(age)

    if travel_insur:
        if place == "國外":
            travel_insur.remove('一日平安專案')
            if period >= 180:
                travel_insur = ['out_day_ques']
        elif place == "國內":
            travel_insur.remove('180天留遊學差旅專案')
            if period <= 30 and period != 1:
                travel_insur.remove('一日平安專案')
            if period == 1:
                travel_insur.remove('e悠遊旅行平安險')
            if period >= 30:
                travel_insur = ['in_day_ques']
    else:
        travel_insur = ['age_ques']
    return travel_insur
            

def travel_reply(person, age, period, place):
    productLIST = res_insurance(age, period, place)
    if "out_day_ques" in productLIST:
        replySTR = t_reply['out_day_ques']
    elif "in_day_ques" in productLIST:
        replySTR = t_reply['in_day_ques']
    elif "age_ques" in productLIST:
        replySTR = t_reply['age_ques'].format(age)
    elif len(productLIST) == 0:
        replySTR = t_reply['no_product']
    elif len(productLIST) == 1:
        if "e悠遊旅行平安險" in productLIST:
            web = eWeb
        elif  "180天留遊學差旅專案" in productLIST:
            web = abroadWeb
        elif "一日平安專案" in productLIST:
            web = oneWeb
        replySTR = "您的方案為：\n" + t_reply['multi_product'].format(*productLIST, web) 
    elif len(productLIST) == 2:
        multi_reply = []
        if "e悠遊旅行平安險" in productLIST:
            ans = reply_e.format(eWeb)
            multi_reply.append(ans) 
        if  "180天留遊學差旅專案" in productLIST:
            ans = reply_180.format(abroadWeb)
            multi_reply.append(ans)
        if "一日平安專案" in productLIST:
            ans = reply_ping.format(oneWeb)
            multi_reply.append(ans)
        replySTR = "目前有**「2個」**方案適合您喔！\n\n"+"\n".join(multi_reply)
    return {'ans': replySTR, 'pd':productLIST}        





# 支付方式
def way_pay(inputSTR):
    if inputSTR:
        if inputSTR in ["信用卡", "活期帳戶", "街口電子支付", "街口支付", "街口"]:
            return reply_pay['yes']
        elif inputSTR == "電子支付":
            return reply_pay['electronic']
        else:
            return reply_pay['three_way']
    else:
        return ""
    

# 給付項目(有哪些給付項目)
def compensation(inputSTR):
    if inputSTR:
        return reply_com
    else:
        return ""




if __name__ == "__main__":
    print(check_place('33歲美國1天'))

    