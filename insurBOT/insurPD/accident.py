from insurance_bot import execLoki
import random
import json




with open("answer/reply_insur_acc.json", encoding="utf-8") as f:
    replyDICT = json.load(f)

# 保障範圍
pingLIST = replyDICT["享保障微型個人傷害保險"]['reply']
xinLIST = replyDICT["心e路平安傷害保險"]['reply']
iCarryLIST = replyDICT["新iCarry傷害保險"]['reply']
accLIST = replyDICT["意外險"]

# 網址
pingWeb = replyDICT["享保障微型個人傷害保險"]['web']
xinWeb = replyDICT["心e路平安傷害保險"]['web']
iCarryWeb = replyDICT["新iCarry傷害保險"]['web']

# 回覆
reply_a = replyDICT['acc_reply']

# 賠償項目
reply_com = replyDICT['compensation']

# 付費方式
reply_pay = replyDICT['way_pay']

# 實支實付等的問題
reply_com_detail = replyDICT['benefit_specific']





def age_filter(age):
    age = int(age)
    possible_insur = []
    if 20 <= age <= 50:
        possible_insur.append("心e路平安傷害保險")
    if 20 <= age <=64:
        possible_insur.append("享保障微型個人傷害保險")
    if 20 <= age <= 55:
        possible_insur.append("新iCarry傷害保險")
    return possible_insur




def res_insurance(age, acc_con):
    insur = age_filter(age)
    w_insur = "享保障微型個人傷害保險"
    icarry = "新iCarry傷害保險"
    e_insur = "心e路平安傷害保險"

    if insur:
        if acc_con:
            if "weak" in acc_con:
                if w_insur in insur:
                    insur.remove(e_insur)
                    insur.remove(icarry)
            elif "traffic" in acc_con:
                
                insur.remove(w_insur)
                if icarry in insur:
                    insur.remove(e_insur)
            elif "high" in acc_con:
                insur.remove(w_insur)
                if icarry in insur:
                    insur.remove(e_insur)
            elif "low" in acc_con:
                insur.remove(w_insur)
                if e_insur in insur:
                    insur.remove(icarry)
            elif "job" in acc_con:
                insur.remove(w_insur)
                if "need_budget" in insur:
                    insur.remove("need_budget")
                if "high" in acc_con:
                    if icarry in insur:
                        insur.remove(e_insur)
                elif "low" in acc_con:
                    if e_insur in insur:
                        insur.remove(icarry)
                else:
                    insur.append('need_budget')
            else:
                insur.clear()
                insur = ['only_budget']
        else:
            insur.clear()
            insur = ['con_lack']
    else:
        insur.clear()
        insur = ['age_ques']
    return insur







def acc_reply(person, age, acc_con):
    productLIST = res_insurance(age, acc_con)
    w_insur = "享保障微型個人傷害保險"
    icarry = "新iCarry傷害保險"
    e_insur = "心e路平安傷害保險"
    replySTR = "沒東西"
    
    if "need_budget" in productLIST:
        productLIST.remove("need_budget")
        replySTR = reply_a['need_budget'].format(age)
    elif "only_budget" in productLIST:
        replySTR = reply_a['only_budget'].format(person, age)
    elif "age_ques" in productLIST:
        replySTR = reply_a['age_ques'].format(age)
    elif "con_lack" in productLIST:
        replySTR = reply_a['con_lack'].format(person, age)

    if len(productLIST) == 1:
        if w_insur in productLIST:
            replySTR = reply_a[w_insur].format(age)
        elif icarry in productLIST:
            replySTR = reply_a[icarry].format(age)
        elif e_insur in productLIST:
            replySTR = reply_a[e_insur].format(age)

    elif len(productLIST) == 2:
        replySTR = reply_a['need_budget'].format(age)
    elif len(productLIST) == 0:
        replySTR = reply_a["no_product"]
    return {'ans':replySTR, 'pd':productLIST}

       

# 付款方式
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



# 給付項目
def compensation(recordDICT):
    product = recordDICT['product']
    if product:
        result = []
        if "享保障微型個人傷害保險" in product :
            ans = random.choice(pingLIST)
            result.append(ans)
    
        elif  "心e路平安傷害保險" in product:
            ans = random.choice(xinLIST)
            result.append(ans)
                      
        elif "新iCarry傷害保險" in product:
            ans = random.choice(iCarryLIST)
            result.append(ans)
        
        elif "意外險" in product:
            ans = random.choice(accLIST)
            result.append(ans)
          
        else:
            replySTR =  ""
        res_sent = "\n".join(result)
        replySTR = reply_com['res_sent'].format(res_sent)
        return replySTR

    elif not product:
        if recordDICT['age'] and recordDICT['acc_con']:
            age = int(recordDICT['age'][0])
            acc_insurance = acc_reply("", age, recordDICT['acc_con'])['pd']
            
            
        elif recordDICT['age'] and not recordDICT['acc_con']:
            return reply_com['age'].format(age)
        
        elif not recordDICT['age'] and recordDICT['acc_con']:
            return reply_com['no_age']
        
        elif not recordDICT['age'] and not recordDICT['acc_con']: 
            return reply_com['no_info']
    

def acc_benefit(recordDICT):
    product = recordDICT['product']
    require = recordDICT['acc_benefit'][0]
    replySTR = ""
    pd = []

    if "list" in require:
        if "gs" in require:
            pd = ['新iCarry傷害保險']
            replySTR = reply_com_detail['list_p']['gs']
        elif "yiliao" in require:
            pd = ['新iCarry傷害保險', '心e路平安傷害保險']
            replySTR = reply_com_detail['list_p']['yiliao']


    elif "accident" in recordDICT['type']:
        if "yn" in require:
            if len(product) == 2:
                if (product[0] and product[1]) in ['新iCarry傷害保險', '心e路平安傷害保險']:
                    replySTR = reply_com_detail['yes']['two_product']

            elif len(product) == 1:
                if "yiliao" in require:
                    if "iCarry" in product[0]:
                        replySTR = reply_com_detail['yes']['yiliao_icarry']
                    elif "心e路平安" in product[0]:
                        replySTR = reply_com_detail['no']['yiliao_e']
                    elif "享保障" in product[0] and "傷害" in product[0]:
                        replySTR = reply_com_detail['yes']['yiliao_xiang']
                elif "gs" in require:
                    if "iCarry" in product[0]:
                        replySTR = reply_com_detail['yes']['gs_icarry']
                    elif "心e路平安" in product[0]:
                        replySTR = reply_com_detail['no']['gs_e_xiang']
                    elif "享保障" in product[0] and "傷害" in product[0]:
                        replySTR = reply_com_detail['yes']['gs_e_xiang']
            elif not product:
                replySTR = reply_com_detail['please_get']

    elif "life" in recordDICT['type']:
        if "yn" in require:
            if "gs" in require:
                replySTR = reply_com_detail['out']['life_gs']
            elif "yiliao" in require:
                replySTR = reply_com_detail['out']['life_yiliao']
        elif "list" in require:
            if "gs" in require:
                replySTR = reply_com_detail['out']['other_gs_list']
            elif "yiliao" in require:
                replySTR = reply_com_detail['out']['life_yiliao_list']

    elif "travel" in recordDICT['type']:
        if "yn" in require:
            if "gs" in require:
                replySTR = reply_com_detail['out']['travel_gs']
            elif "yiliao" in require:
                replySTR = reply_com_detail['out']['travel_yiliao']
        elif "list" in require:
            if "gs" in require:
                replySTR = reply_com_detail['out']['other_gs_list']
            elif "yiliao" in require:
                replySTR = reply_com_detail['out']['travel_yiliao_list']

    if pd:
        recordDICT['product'] = pd
        recordDICT['type'] = ['accident']
    recordDICT['temp_ans'] = replySTR      
    return recordDICT
                
        







if __name__ == "__main__":
    recordDICT = {'product':['心iCarry'], "acc_benefit":['gs_yn']}
    print(acc_benefit(recordDICT))