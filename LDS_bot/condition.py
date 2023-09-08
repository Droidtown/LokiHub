import logging
import re
import json

from A_background.A_background import execLoki as background_execLoki
from B_environment.B_environment import execLoki as environment_execLoki
from C_behavior.Under_1.Under_1 import execLoki as under1_execLoki
from C_behavior.Above_1.Above_1 import execLoki as above1_execLoki
from C_behavior.Above_2.Above_2 import execLoki as above2_execLoki
from C_behavior.Above_3.Above_3 import execLoki as above3_execLoki
from C_behavior.Above_4.Above_4 import execLoki as above4_execLoki
from C_behavior.Above_5.Above_5 import execLoki as above5_execLoki
from C_behavior.Above_6.Above_6 import execLoki as above6_execLoki

with open('behavior_tags.json', encoding='utf-8') as f:
    question_tags = json.load(f)

with open('behavior_questions.json', encoding='utf-8') as f:
    meta_data = json.load(f)

with open('behavior_questions.json', encoding='utf-8') as f:
    behavior_questions = json.load(f)

reverse_list = {
    "under1":["q11"],
    "above1":["q5"],
    "above2":["q4", "q7"],
    "above3":["q2", "q10", "q12"],
    "above4":["q1", "q5", "q9"],
    "above5":["q2", "q3", "q5", "q7"],
    "above6":["q1", "q3", "q8", "q11"]
}

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def operateLoki(context, inputSTR, filterList=[]):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = filterList
    if context == "background":
        resultDICT = background_execLoki(inputLIST, filterLIST)
    elif context == "environment":
        resultDICT = environment_execLoki(inputLIST, filterLIST)
    elif context == "under1":
        resultDICT = under1_execLoki(inputLIST, filterLIST)
    elif context == "above1":
        resultDICT = above1_execLoki(inputLIST, filterLIST)
    elif context == "above2":
        resultDICT = above2_execLoki(inputLIST, filterLIST)
    elif context == "above3":
        resultDICT = above3_execLoki(inputLIST, filterLIST)
    elif context == "above4":
        resultDICT = above4_execLoki(inputLIST, filterLIST)
    elif context == "above5":
        resultDICT = above5_execLoki(inputLIST, filterLIST)
    else:
        resultDICT = above6_execLoki(inputLIST, filterLIST)

    logging.debug("Loki Result => {}".format(resultDICT))
    
    return resultDICT

def order_rule(x):
    order = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13"]
    return order.index(x)

def get_key_from_value(dict, val):
    resultList = []
    for key, value in dict.items():
        if val == value:
            resultList.append(key)
    return resultList 

def give_advice(age, final_data):
    target_age = age
    accpetance = len(get_key_from_value(final_data["behavior"], True))
    if target_age//12 == 0:
        if accpetance >= 10:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance <= 9 and accpetance >= 6:
            result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        elif accpetance <= 5:
            if target_age >= 6 and target_age < 11:
                result = "您可以再觀察四至六個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            elif target_age > 11:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else:
            result = "目前孩子正處理語言發展的準備前期，建議您可以多跟孩子互動，並持續觀察孩子與您的互動表現，待孩子大一點，如：十個月大或近一歲時，若還不能發出一些不同的聲音時，再到醫療院所進行語言篩檢。"

    elif target_age//12 == 1:
        if accpetance >= 6:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 4 or accpetance == 5:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            if target_age >= 12 and target_age <= 18:
                if len(get_key_from_value(final_data["background"], False)) == 0:
                    result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
                else:
                    result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif target_age >= 19:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    
    elif target_age//12 == 2:
        if accpetance >= 8:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 4 and accpetance <= 7:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    
    elif target_age//12 == 3:
        if accpetance >= 8:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 4 and accpetance <= 7:
            if len(get_key_from_value(final_data["background"], False)) == 0:
                result = "您可以再觀察兩到三個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
            else:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            
    elif target_age//12 == 4:
        if accpetance >= 7:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance > 3 and accpetance <= 6:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"

    elif target_age//12 == 5:
        if accpetance >= 6:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 4 or accpetance == 5:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"

    elif target_age//12 == 6:
        if accpetance >= 10:
            result = "推測您的孩子符合同齡孩童語言發展，建議您或照顧者持續在生活中營造更多與孩子互動的機會，同時也要持續觀察孩子的語言表現哦!"
        elif accpetance == 8 or accpetance == 9:
            if len(get_key_from_value(final_data["background"], False)) != 0:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            elif final_data["environment"]["3c"] == True or final_data["environment"]["school"] == False:
                result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
            else:
                result = "您可以再觀察一到兩個月，若孩子的語言表現無明顯變化則建議您或照顧者可帶孩子至醫療院所接受完整評估。"
        else :
            result = "建議您或照顧者可帶孩子至醫療院所接受完整評估，也需持續在生活中營造更多與孩子互動的機會以刺激孩子語言發展。"
    return result

def condition_control(dicts, context, msgSTR):
    data = dicts
    # Part A 處理
    if context == "background":
        cont = "background"
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data[context], "None") 
        
        # 偵測 intent
        if "half" in data[context].keys():
            resultDICT = operateLoki(context, msgSTR, ["recheck"])
            data[context].pop("half")
        else:
            if len(waiting_question) == 5:
                resultDICT = operateLoki(context, msgSTR, ["age"])
            elif len(waiting_question) == 4:
                resultDICT = operateLoki(context, msgSTR, ["ten_month"])
            elif len(waiting_question) == 3:
                resultDICT = operateLoki(context, msgSTR, ["weight"])
            elif len(waiting_question) == 2:
                resultDICT = operateLoki(context, msgSTR, ["congenital_disease", "yes_no"])
                if "yes_no" in resultDICT.keys() and "congenital_disease" not in resultDICT.keys():
                    resultDICT["congenital_disease"] = resultDICT["yes_no"]
                    resultDICT["response"] = ["了解，再來想確認一下孩子的親戚是否有家族遺傳性相關疾病呢？"]
                    resultDICT.pop("yes_no")
            elif len(waiting_question) == 1:
                resultDICT = operateLoki(context, msgSTR, ["genetic_disease", "yes_no"])
                if "yes_no" in resultDICT.keys() and "genetic_disease" not in resultDICT.keys():
                    if resultDICT["yes_no"][0] == False:
                        resultDICT["genetic_disease"] = [False]
                        resultDICT["response"] = ["好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?"]
                        resultDICT.pop("yes_no")
                    else:
                        resultDICT["response"] = ["那麼是孩子的哪位親人有什麼樣的遺傳性疾病呢？"]
                        resultDICT.pop("yes_no")
        
        # 資料寫入字典
        for key in resultDICT:
            if key != "response":
                data[context][key] = resultDICT[key][0]
            else:
                data[context][key] = resultDICT[key][-1]

        # 確認 Part A 資料是否收集完畢
        if len(get_key_from_value(data[context], "None")) == 0:
            data[context]["a"] = True

    # Part B 處理
    elif context == "environment":
        cont = "environment"
        # 檢查目前提問進展
        waiting_question = get_key_from_value(data[context], "None")

        # 偵測 intent
        if len(waiting_question) == 2:
            resultDICT = operateLoki(context, msgSTR, ["school", "yes_no"])
            if "yes_no" in resultDICT.keys() and "school" not in resultDICT.keys():
                resultDICT["school"] = resultDICT["yes_no"]
                resultDICT["response"] = ["那麼孩子每天使用3C產品(包括：手機、平版、電腦、電視)的總時間有超過2小時嗎?"]
                resultDICT.pop("yes_no")
            elif "yes_no" in resultDICT.keys() and "school" in resultDICT.keys():
                resultDICT.pop("yes_no")

        elif len(waiting_question) == 1:
            resultDICT = operateLoki(context, msgSTR, ["3C", "yes_no"])
            if "yes_no" in resultDICT.keys() and "3c" not in resultDICT.keys():
                resultDICT["3c"] = resultDICT["yes_no"]
                resultDICT["response"] = ["好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對他平常的行為表現作更深入的了解囉。"]
                resultDICT.pop("yes_no")
            elif "yes_no" in resultDICT.keys() and "3C" in resultDICT.keys():
                resultDICT.pop("yes_no")

        # 資料寫入字典
        for key in resultDICT:
            if key != "response":
                data[context][key] = resultDICT[key][0]
            else:
                data[context][key] = resultDICT[key][-1]
            
        # 確認 Part B 資料是否收集完畢
        if len(get_key_from_value(data[context], "None")) == 0:
            data[context]["b"] = True
        if "b" in data[context].keys() and data[context]["b"] == True:
            age = data["background"]["age"] // 12
            if age == 0:
                data[context]["response"] =data[context]["response"] + "\n" + meta_data["under1"]["q1"]
            else:
                new_context = "above" + str(age)
                data[context]["response"] =data[context]["response"] + "\n" + meta_data[new_context]["q1"]
    
    # Part C 處理
    else:
        cont = "behavior"
        # 檢查目前提問進展
        amount = meta_data[context]["amount"]
        waiting_question = get_key_from_value(data["behavior"], "None")
        waiting_question.sort(key=order_rule)
        
        # 偵測 intent
        resultDICT = operateLoki(context, msgSTR, ["yes_no", question_tags[context][waiting_question[0]]])
        if "yes_no" in resultDICT.keys() and waiting_question[0] not in resultDICT:
            if waiting_question[0] not in reverse_list[context]:
                resultDICT[waiting_question[0]] = resultDICT["yes_no"]
                resultDICT.pop("yes_no")
            else:
                if resultDICT["yes_no"] == [True]:
                    resultDICT[waiting_question[0]] = [False]
                    resultDICT.pop("yes_no")
                else:
                    resultDICT[waiting_question[0]] = [True]
                    resultDICT.pop("yes_no")

        elif "yes_no" in resultDICT.keys() and waiting_question[0] in resultDICT:
            resultDICT.pop("yes_no")
        
        print(waiting_question)

        # 資料寫入字典
        for key in resultDICT:
            if key != "response":
                data["behavior"][key] = resultDICT[key][0]
            else:
                data["behavior"][key] = resultDICT[key][-1]

        if len(get_key_from_value(data["behavior"], "None")) == 13-amount:
            data["behavior"]["response"] = give_advice(data["background"]["age"], data)
            data["behavior"]["c"] = True
        else:
            if "response" not in resultDICT.keys():
                next_q = get_key_from_value(data["behavior"], "None")[0]
                data["behavior"]["response"] = behavior_questions[context][next_q]

        # 判斷對話是否結束，如果結束就給建議
        if "c" in data["behavior"].keys() and data["behavior"]["c"] == True:
            data["behavior"]["response"] = give_advice(data["background"]["age"], data)

    return data[cont]

if __name__ == "__main__":
    dicts = {'a': True,
 'b': True,
 'background': {'a': True,
                'age': 76,
                'congenital_disease': False,
                'genetic_disease': False,
                'response': '好的，接下來想針對孩子的生活環境跟您做一些確認。\n不知道孩子是不是已經上托嬰中心或幼兒園了呢?',
                'ten_month': True,
                'weight': True},
 'behavior': {'q1': True,
              'q10': 'None',
              'q11': 'None',
              'q12': 'None',
              'q13': 'None',
              'q2': True,
              'q3': True,
              'q4': True,
              'q5': True,
              'q6': True,
              'q7': False,
              'q8': 'None',
              'q9': 'None',
              'response': '目前我們已經完成大部分的問題了...接下來剩幾個而已唷～請問，您的孩子說話時，每十句會出現至少兩句的口吃、不流暢的情形嗎？'},
 'c': False,
 'environment': {'3c': False,
                 'b': True,
                 'response': '好的。關於孩子的一些基本資訊都蒐集完畢，接著要針對他平常的行為表現作更深入的了解囉。\n'
                             '孩子說話時的口齒不清，需要親近家人翻譯後他人才聽得懂嗎？',
                 'school': True},
 'latestQuest': '',
 'response': []} #弄個測試用的回傳字典
    context = "above6"
    msgSTR = "不會"
    resultDICT = condition_control(dicts, context, msgSTR)
    print(resultDICT)