from insurance_bot import execLoki
import json
import re
import random




with open("answer/reply_insur_life.json", encoding="utf-8") as f:
    replyDICT = json.load(f)



# 保險
high_life_list = replyDICT["享保障定期壽險"]
small_life_list = replyDICT["享保障小額終身壽險"]
weak_life_list = replyDICT["享保障微型個人定期壽險"]
is_life_list = replyDICT["心iLife一年期定期壽險 & 享保障小額終身壽險"]

# 條件不符
over74_life_list = replyDICT[">74"]
noMatch_life_list = replyDICT["沒有符合條件"]
under20_life_list = replyDICT["未滿20"]

# 專案保障的項目
claimHigh_life_list = replyDICT["享保障定期壽險的給付項目"]
claimSmall_life_list = replyDICT["享保障小額終身壽險的給付項目"]
claimWeak_life_list = replyDICT["享保障微型個人定期壽險的給付項目"]

# 保障
reply_com = replyDICT['compensation']

# 付費方式
reply_pay = replyDICT['way_pay']

# 終身or定期
reply_life_regular = replyDICT['life_period']



def res_insurance(age, resultDICT, recordDICT):
    life = ["心iLife一年期定期壽險","享保障小額終身壽險","享保障定期壽險","享保障微型個人定期壽險"]
    age = int(age)
    for idx, con in enumerate(recordDICT['life_con']):
        if '_identity' in con:
            recordDICT['life_con'][idx] = con.replace("_identity", "")

    if age < 20:
        under20Ans = random.choice(under20_life_list)
        return {"ans":under20Ans, "pd":None}
    if age > 74:
        over74Ans = random.choice(over74_life_list)
        return {"ans":over74Ans, "pd":None}
    elif age > 64:     
        if "weak" not in recordDICT["life_con"]:
            smallAns = random.choice(small_life_list)
            return {"ans":smallAns, "pd":["享保障小額終身壽險"]}
        elif "weak" in recordDICT["life_con"]:
            noMatch_ans = random.choice(noMatch_life_list)
            return {"ans":noMatch_ans, "pd":None}         
    elif age > 50:        
        life.remove("心iLife一年期定期壽險")
        if "weak" in recordDICT["life_con"]:
            weakAns = random.choice(weak_life_list)
            return {"ans":weakAns, "pd":["享保障微型個人定期壽險"]}
        elif "low" in recordDICT["life_con"]:
            smallAns = random.choice(small_life_list)
            return {"ans":smallAns, "pd":["享保障小額終身壽險"]}          
        elif "high" in recordDICT["life_con"]:
            highAns = random.choice(high_life_list)
            return {"ans":highAns, "pd":["享保障定期壽險"]}
        elif resultDICT['low'] == True:
            isAns = random.choice(is_life_list)
            return {"ans":isAns, "pd":["心iLife一年期定期壽險", "享保障小額終身壽險"]}             
        elif resultDICT['high'] == True:
            highAns = random.choice(high_life_list)
            return {"ans":highAns, "pd":["享保障定期壽險"]} 
        else:
            noMatch_ans = random.choice(noMatch_life_list)
            return {"ans":noMatch_ans, "pd":None} 
    if 20 <= age <= 50:       
        if "weak" in recordDICT["life_con"]:
            weakAns = random.choice(weak_life_list)
            return {"ans":weakAns, "pd":["享保障微型個人定期壽險"]}
        elif "low" in recordDICT["life_con"]:
            isAns = random.choice(is_life_list)
            return {"ans":isAns, "pd":["心iLife一年期定期壽險", "享保障小額終身壽險"]}
        elif "high" in recordDICT["life_con"]:
            highAns = random.choice(high_life_list)
            return {"ans":highAns, "pd":["享保障定期壽險"]}       
        else:
            noMatch_ans = random.choice(noMatch_life_list)
            return {"ans":noMatch_ans, "pd":None}    



def compensation(resultDICT, recordDICT):
    product = recordDICT['product']
    if product:
        ans_life = reply_com['final_ans']
        if product == ['心iLife一年期定期壽險', '享保障微型個人定期壽險', '享保障定期壽險']:
            benefit_three = reply_com['three_pd']
            return ans_life.format(benefit_three)


        elif product == ["心iLife一年期定期壽險","享保障小額終身壽險"]:
            benefit_special = reply_com['xinIlife']
            return ans_life.format(benefit_special)
        
        elif product == ["享保障小額終身壽險"]:
            claimSmall_ans = random.choice(claimSmall_life_list)
            return ans_life.format(claimSmall_ans)
                      
        elif product == ["享保障微型個人定期壽險"]:
            claimWeak_ans = random.choice(claimWeak_life_list)
            return ans_life.format(claimWeak_ans)
            
        elif product == ["享保障定期壽險"]:
            claimHigh_ans = random.choice(claimHigh_life_list)
            return ans_life.format(claimHigh_ans)
        else:
            return "沒辦法提供更多資訊喔～"
        
    elif not product:
        if recordDICT['age'] and recordDICT['life_con']:
            age = int(recordDICT['age'][0])
            life_insurance = res_insurance(age, resultDICT, recordDICT)['ans'] # 記得檢查每一個並且加上字典的key: ans
            
        elif recordDICT['age'] and not recordDICT['life_con']: 
            return reply_com['age'].format(age)
        
        elif not recordDICT['age'] and recordDICT['life_con']:
            return reply_com['no_age']
        
        elif not recordDICT['age'] and not recordDICT['life_con']: 
            return reply_com['no_info']



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



def life_period(recordDICT):
    type = recordDICT['type']
    product = recordDICT['product']
    ques = recordDICT['life_period'][0]
    con = recordDICT['life_con']
    replySTR = ""
    pd = []

    if "life" in recordDICT['type']:
    # product是定期還是終身
        if product and "or_" in ques:
            if len(product) == 1:
                if "定期" in product[0]:
                    replySTR = reply_life_regular['or']['regular']
                elif "終身" in product[0]:
                    replySTR = reply_life_regular['or']['life']
            elif len(product) == 2:
            
                replySTR = reply_life_regular['or']['two_product']
                
        elif product and "yn" in ques:
            if len(product) == 1:
                if "定期" in product[0]:
                    if "regular" in ques:
                        replySTR = reply_life_regular['yes']['regular']
                    elif "life" in ques:
                        replySTR = reply_life_regular['no']['regular']
                elif "終身" in product[0]:
                    if "regular" in ques:
                        replySTR = reply_life_regular['no']['life']
                    elif "life" in ques:
                        replySTR = reply_life_regular['yes']['life']
            elif len(product) == 2:
                replySTR = reply_life_regular['or']['two_product']    

        elif 'list' in ques:
            if "regular" in ques:
                replySTR = reply_life_regular['list_p']['regular']
                pd =['心iLife一年期定期壽險', '享保障微型個人定期壽險', '享保障定期壽險']
            elif "life" in ques:
                replySTR = reply_life_regular['list_p']['life']
                pd = ['享保障小額終身壽險']
            
        # 附加狀態題：想要定期且預算低 / 定期且保障多 / 定期且特殊身份
        elif 'combine' in ques and con:
            if "life" in ques:            
                replySTR = reply_life_regular['list_p']['life']
                pd = ['享保障小額終身壽險']
            elif "regular" in ques:
                if 'weak' in con:
                    replySTR = random.choice(reply_life_regular['combine']['r_weak'])
                    pd = ['享保障微型個人定期壽險']
                elif 'low' in con:
                    replySTR = random.choice(reply_life_regular['combine']['r_low'])
                    pd = ['心iLife一年期定期壽險']
                elif 'high' in con:
                    replySTR = random.choice(reply_life_regular['combine']['r_high'])
                    pd = ['享保障定期壽險']
    else:
        replySTR = reply_life_regular['out']
    if pd:
        recordDICT['product'] = pd
        recordDICT['type'] = ['life']
    recordDICT['temp_ans'] = replySTR
    return recordDICT








            
if __name__ == "__main__":
        
    recordDICT = execLoki("我23歲，是一位上班族")
    print(recordDICT)
    ans = res_insurance(recordDICT['age'][0], recordDICT)
    print(ans)