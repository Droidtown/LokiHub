from insurance_bot import execLoki

import json
import random
from insurPD.travel import travel_reply as travel
from insurPD.accident import acc_reply as acc
from insurPD.life import res_insurance as life


with open("answer/reply_feature_acc.json", encoding="utf-8") as f:
    acc_feature = json.load(f)

with open("answer/reply_feature_life.json", encoding="utf-8") as f:
    life_feature = json.load(f)

with open("answer/reply_feature_travel.json", encoding="utf-8") as f:
    travel_feature = json.load(f)

with open("answer/reply_general.json", encoding="utf-8") as f:
    general_reply = json.load(f)

with open("answer/reply_no_offer.json", encoding="utf-8") as f:
    no_offer_reply = json.load(f)




# 資訊 放入 discord 裡
def record_to_discord(resultDICT, recordDICT, resetFunc):
    if recordDICT['type']:

        if "product" in resultDICT:
            recordDICT['product'] = resultDICT['product']
        
        if "change" in resultDICT:
            print("幫人問")
            recordDICT = resetFunc
            recordDICT['age'] = None # 因為之前有存所以要清空
            for new in recordDICT:
                if new in resultDICT:
                    recordDICT[new] = resultDICT[new]

        if "switch_insur" in resultDICT:
            print("換另外一個險")
            age_keep = recordDICT['age']
            recordDICT = resetFunc
            recordDICT['age'] = age_keep
            for s in recordDICT:
                if s in resultDICT:
                    recordDICT[s] = resultDICT[s]

        # 更改人(代表幫另外一個人問)
        if "person" in resultDICT:
            if recordDICT['person'] != resultDICT['person']:
                print("替別人問/換人")
                recordDICT = resetFunc
                recordDICT['person_change'] = True
                for p in recordDICT:
                    if p in resultDICT:
                        recordDICT[p] = resultDICT[p] 


        if resultDICT['type'] and recordDICT['type'] != resultDICT['type']:
            print("險別/換新: 但是歲數保留")
            age_keep = recordDICT['age']
            recordDICT = resetFunc
            for diff in recordDICT:
                if diff == 'age' and recordDICT['age']!= None:
                    recordDICT['age'] = age_keep
                else:
                    if diff in resultDICT:
                        recordDICT[diff] = resultDICT[diff]

        else:
            print("有保險/補資訊")
            
            # 更改年齡
            if 'age' in resultDICT and recordDICT['age']:
                if len(resultDICT) >= 2 and recordDICT['age'] != resultDICT['age']:
                    print("年齡/換新")
                    recordDICT = resetFunc
                    recordDICT['age_change'] = True
                    for diff in recordDICT:
                        if diff in resultDICT:
                            recordDICT[diff] = resultDICT[diff]

                   


            if "travel" in recordDICT['type']:
                for t in ['place', 'period', 'age', 'way_pay', 'benefit', "feature", "acc_benefit", "life_period", "no_offer", "strange"]:
                    if t in resultDICT:
                        # if recordDICT['age'] != resultDICT['age']:
                        #     recordDICT = resetFunc
                        #     recordDICT['age_change'] = True
                        #     for diff in recordDICT:
                        #         if diff in resultDICT:
                        #             recordDICT[diff] = resultDICT[diff]

                        if recordDICT[t] != resultDICT[t] and recordDICT[t] != None:
                            if t != "acc_benefit":
                                print('travel: give a new template')      
                                recordDICT = resetFunc
                                recordDICT['type'] = ['travel']
                                recordDICT[t] = resultDICT[t]
                        elif recordDICT[t] == None:
                            print('travel: add detail info')
                            recordDICT[t] = resultDICT[t]


                        


            if "life" in recordDICT['type']:
                for l in ['life_con', 'age', 'way_pay', 'benefit', "feature", "acc_benefit", "life_period", "no_offer", "strange"]:
                    if l in resultDICT:
                        if l== 'life_con' and recordDICT['life_con']:
                            print('當條件有追問的時候')
                            recordDICT['life_con'].extend(resultDICT['life_con'])

                        elif recordDICT[l] != resultDICT[l] and recordDICT[l] != None:
                            if a != "acc_benefit":
                                print("資訊不同/換新_壽險")                        
                                recordDICT = resetFunc
                                recordDICT['type'] = ['life']
                                recordDICT[l] = resultDICT[l]
                        elif recordDICT[l] == None:
                            print('其他狀況，就直接補資訊')
                            recordDICT[l] = resultDICT[l]




            if "accident" in recordDICT['type']:
                for a in ['acc_con', 'age', 'way_pay', 'benefit', "feature", "acc_benefit", "life_period", "no_offer", "strange"]:
                    if a in resultDICT:    
                        if a == 'acc_con' and recordDICT['acc_con']:
                            print('當條件有追問的時候')
                            recordDICT['acc_con'].extend(resultDICT['acc_con'])
                        
                        elif recordDICT[a] != resultDICT[a] and recordDICT[a] != None:
                            if a != "acc_benefit":
                                print("資訊不同/換新_意外險")
                                recordDICT = resetFunc
                                recordDICT['type'] = ['accident']
                                recordDICT[a] = resultDICT[a]

                        elif recordDICT[a] == None:
                            print('其他狀況，就直接補資訊')
                            recordDICT[a] = resultDICT[a]


            

    elif not recordDICT['type']:
        print("一開始")
        for i in recordDICT:
            if i in resultDICT:
                recordDICT[i] = resultDICT[i]

    return recordDICT



# 旅平險的回覆
def travel_response(person, recordDICT, resetFunc):

    travel_info = {"age":["歲數", "年齡"], "place":['地點', "地方", '國內 or 國外'], "period":["天數"]}
    unknown_info = [k for k in travel_info if recordDICT[k] == None]
    known_info = [i for i in travel_info if i not in unknown_info]
    
    for idx, info in enumerate(unknown_info):
        unknown_info[idx] = info.replace(info, random.choice(travel_info[info]))
    
    for idx, info in enumerate(known_info):
        known_info[idx] = info.replace(info, random.choice(travel_info[info]))

    if len(known_info) == 0:
        return general_reply['travel']['begin'].format(person)
    elif len(known_info) == 1:
        return general_reply['travel']['lack1'].format(person, *known_info, *unknown_info)
    elif len(known_info) == 2:
        return general_reply['travel']['lack2'].format(person, *known_info, *unknown_info)
    elif len(known_info) == 3:
        precise_insur = travel(person, recordDICT['age'][0], recordDICT['period'][0], recordDICT['place'][0])['ans']
        recordDICT['product'] = travel(person, recordDICT['age'][0], recordDICT['period'][0], recordDICT['place'][0])['pd']
        recordDICT = resetFunc
        return precise_insur
        




# 意外險回覆
def accident_response(person, resultDICT, recordDICT, resetFunc):
    acc_info = {"age":["歲數", "年齡"], "acc_con":{'traffic':'交通方式(騎車、開車等等)', 'job':'職業', 'high':'加倍保障/保障多', 'low':'預算少/價格實惠', 'weak':'特殊身份'}}

    unknown_info = [k for k in acc_info if recordDICT[k] == None]
    known_info = [i for i in acc_info if i not in unknown_info]
    final_kn = []
    final_unk = []


    if known_info:
        if 'acc_con' in known_info:
            for key in acc_info['acc_con']:
                if recordDICT['acc_con'] and key in recordDICT['acc_con']:
                    final_kn.append(acc_info['acc_con'][key])
            if len(final_kn) > 1:
                final_kn ="\n".join(final_kn)
            elif len(final_kn) == 1:
                final_kn = final_kn[0]
        if 'age' in known_info:
            final_kn = f"{random.choice(acc_info['age'])}目前是 {recordDICT['age'][0]}歲 (若是要修改年齡可以直接輸入喔！💁🏻‍♀️)"
    if unknown_info:
        if 'acc_con' in unknown_info:
            final_unk.append(general_reply['accident']['need_con'])
        if 'age' in unknown_info:
            final_unk.append(random.choice(acc_info['age']))



    if len(known_info) == 0:
        return general_reply['accident']['begin'].format(person)
    if len(known_info) == 1:
        print('已知一個資訊')
        return general_reply['accident']['lack1'].format(person, final_kn, *final_unk)
    elif len(known_info) == 2:
        print('知道兩個')
        if recordDICT['acc_con']:
            precise_insur = acc(person, recordDICT['age'][0], recordDICT['acc_con'])['ans']
            recordDICT['product'] = acc(person, recordDICT['age'][0], recordDICT['acc_con'])['pd']
            recordDICT = resetFunc
            return precise_insur
        




# 壽險的回覆
def life_response(person, resultDICT, recordDICT, resetFunc): 
    life_info = {"age":["歲數", "年齡"], "life_con": {'high':'加倍保障/保障多', 'low':'預算少/價格實惠', 'weak':'特殊身份', 'high_identity':'狀態(or身份)', 'low_identity':'狀態(or身份)'}}

    unknown_info = [k for k in life_info if recordDICT[k] == None]
    known_info = [i for i in life_info if i not in unknown_info]
    final_kn = []
    final_unk = []

    if known_info:
        if 'life_con' in known_info:
            for key in life_info['life_con']:
                if recordDICT['life_con'] and key in recordDICT['life_con']:
                    final_kn.append(life_info['life_con'][key])
            if len(final_kn) > 1:
                final_kn ="\n".join(final_kn)
            elif len(final_kn) == 1:
                final_kn = final_kn[0]

        if 'age' in known_info:
            final_kn = f"{random.choice(life_info['age'])}目前是 {recordDICT['age'][0]}歲 (若是要修改年齡可以直接輸入喔！💁🏻‍♀️）"

    if unknown_info:
        if 'life_con' in unknown_info:
            final_unk.append(general_reply['life']['need_con'])
        if 'age' in unknown_info:
            final_unk.append(random.choice(life_info['age']))
    
    if len(known_info) == 0:
        return general_reply['life']['begin'].format(person)
    if len(known_info) == 1:
        return general_reply['life']['lack1'].format(person, final_kn, *final_unk)
    elif len(known_info) == 2:
        # age & life_con(weak, low, high)
        if recordDICT['life_con']:
            precise_insur = life(recordDICT['age'][0], resultDICT, recordDICT)['ans']
            recordDICT['product'] = life(recordDICT['age'][0], resultDICT, recordDICT)['pd']
            recordDICT = resetFunc
            return precise_insur
        




def feature_insur(recordDICT):
    product = recordDICT['product']
    feature = recordDICT['feature']
    if feature:
        save = []
        if len(product) == 0:
            res = "這個東西的特色目前還尚未建立，可以直接敘述其他問題喔！(如：我想保旅平險)"
        elif len(product) == 1:
            p = product[0]  # Define p here
            if p in life_feature:
                res = f"**{p}**的特色為！\n{random.choice(life_feature[p])}"
            elif p in acc_feature:
                res = f"**{p}**的特色為！\n{random.choice(acc_feature[p])}"
            elif p in travel_feature:
                res = f"**{p}**的特色為！\n{random.choice(travel_feature[p])}"
        elif len(product) == 2:
            if product[0] in life_feature and product[1] in life_feature:
                res = random.choice(life_feature[" & ".join(product)])
            elif product[0] in acc_feature and product[1] in acc_feature:
                for p in product:
                    save.append(f"**{p}**的特色為！\n{random.choice(acc_feature[p])}")  # Fixed parentheses here
                res = "\n\n".join(save)
            elif product[0] in travel_feature and product[1] in travel_feature:
                for p in product:
                    save.append(f"**{p}**的特色為！\n{random.choice(travel_feature[p])}")  # Fixed parentheses here
                res = "\n\n".join(save)
        elif len(product) == 3:
            if product[0] in life_feature and product[1] in life_feature and product[2] in life_feature:
                res = life_feature[" & ".join(product)][0]

    return res



def no_offer(recordDICT):
    ques = recordDICT['no_offer'][0]
    if ques == 'baoe':
        replySTR = random.choice(no_offer_reply['保額'])
    elif ques == 'nianqi':
        replySTR = random.choice(no_offer_reply['年期'])
    elif ques == 'fuyue':
        replySTR = random.choice(no_offer_reply['附約'])
    elif ques == 'fenlei':
        replySTR = random.choice(no_offer_reply['職業分類'])
    elif ques == 'yusuan':
        replySTR = random.choice(no_offer_reply['預算'])
    elif ques == 'peichang':
        replySTR = random.choice(no_offer_reply['賠償'])
    elif ques == 'shisuan':
        replySTR = random.choice(no_offer_reply['保費試算'])
    elif ques == 'out':
        replySTR = random.choice(no_offer_reply['沒有險'])
    elif ques == "xianzhi":
        replySTR = random.choice(no_offer_reply['限制'])
    return replySTR




    
    





    




