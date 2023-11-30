#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import random
import re
from datetime import datetime
from pprint import pprint
from ArticutAPI import Articut

# 追加問題
from insurPD.travel import way_pay as travel_pay
from insurPD.travel import compensation as travel_comp
from insurPD.accident import compensation as acc_comp
from insurPD.accident import way_pay as acc_pay
from insurPD.life import compensation as life_comp
from insurPD.life import way_pay as life_pay

# 特殊特色
from insurPD.accident import acc_benefit
from insurPD.life import life_period


# 回覆
from insurance_bot import execLoki
from toFormat import record_to_discord, travel_response, accident_response, life_response, feature_insur, no_offer






with open(r"account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())
articut = Articut(accountDICT['username'], accountDICT['api_key'])

logging.basicConfig(level=logging.DEBUG)


def getLokiResult(inputSTR): # 拿到的東西送去給Loki
    resultDICT = execLoki(inputSTR) # Loki結果的字典
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

def check_dict_values(dictionary):
    for value in dictionary.values():
        if value != None or value != "":
            return False
    return True

def check_place(msgSTR):
    msgSTR = msgSTR.replace("，", "").replace("。", "")
    sent = articut.parse(msgSTR)['result_obj'][0]
    place = []
    for check in range(len(sent)):
        if "LOCATION" in sent[check]['pos']:
            if sent[check]['text'] != "保定":
                place.append(sent[check]['text'])
    return place

def reply_single_con(recordDICT):
    life_con = recordDICT['life_con']
    acc_con = recordDICT['acc_con']
    if life_con == None:
        life_con = []
    if acc_con == None:
        acc_con = []
        
    life_con.extend(acc_con)
    cond = []
    for i in life_con:
        if i not in cond:
            cond.append(i)
    return cond



class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID): # MSC, multi session conversation 多輪對話
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = {    "id": messageAuthorID,
                             "updatetime" : datetime.now(),
                             "latestQuest": "",
                             "type":None,
                             "unknown":None,
                             "age":None,
                             "place":None,
                             "period":None,
                             "life_con":None,
                             "acc_con":None,
                             "way_pay":None,
                             "benefit":None,
                             "product":None,
                             "feature":None,
                             "change":None,
                             "life_period":None,
                             "acc_benefit":None,
                             "no_offer":None,
                             "strange":None,
                             "switch_insur":None,
                             "person":None
        }
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "type":None,
                             "unknown":None,
                             "age":None,
                             "place":None,
                             "period":None,
                             "life_con":None,
                             "acc_con":None,
                             "way_pay":None,
                             "benefit":None,
                             "product":None,
                             "feature":None,
                             "change":None,
                             "life_period":None,
                             "acc_benefit":None,
                             "no_offer":None,
                             "strange":None,
                             "switch_insur":None,
                             "person":None
        }
        self.mscDICT = { #userid:templateDICT
            
        }
        # ####################################################################################
        
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "要跟我打招呼才能啟動我呦～(可以跟我say hi)✨😎"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。

            elif msgSTR in ["哈囉","嗨","你好","您好"] or any(greet in msgSTR.lower() for greet in ["hi","hello"]): # 收斂（把變化量縮小）
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys(): # 看這個人有沒有跟我們講過話
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = "怎麼又跟我hi一次了呢～可以直接問我問題喔～🤣\n\n我們提供「意外險、旅平險、壽險」的方案推薦，可以直接敘述需求就好了喔~\n\n【範例】：\n1. 單一資訊：我想保壽險 or 我今年20歲\n2. 多樣資訊：我今年25歲想去日本玩5天\n\n單一資訊可以依據提示內容，回答補充需要的資訊。而多樣資訊則是根據您的不同資訊，直接提供方案。（但如果訊息有所缺漏，也會請您再提供～）"
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = f" {msgSTR.title()}~   **{message.author}**😆\n可以根據以上圖片指示告訴我你需要什麼呦！"
                    pic = discord.File("picture/intro_pic.png")
                    await message.reply(file = pic)      
# ##########非初次對話：這裡用 Loki 計算語意
            else:
                
                if message.author.id in self.mscDICT.keys():

                    # 關鍵字補資訊
                    if self.mscDICT[message.author.id]['age'] == None and msgSTR.isnumeric():
                        msgSTR = msgSTR.replace(msgSTR, f"{msgSTR}歲")
                    if not self.mscDICT[message.author.id]['period'] and self.mscDICT[message.author.id]['place'] and self.mscDICT[message.author.id]['age'] and msgSTR.isnumeric():
                        msgSTR = msgSTR.replace(msgSTR, f"{msgSTR}天")
                    if not self.mscDICT[message.author.id]['place'] and check_place(msgSTR):
                        msgSTR = msgSTR.replace(check_place(msgSTR)[0], f"去{check_place(msgSTR)[0]}旅行")
                    
                    
                    resultDICT = getLokiResult(msgSTR)
                    logging.debug("######\nLoki 處理結果如下：")
                    logging.debug(resultDICT)
                    self.mscDICT[message.author.id] = record_to_discord(resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                    print(self.mscDICT)
                    print(self.mscDICT[message.author.id])



                    # 若沒有追加問題就把已經得出完整方案的險清空 
                    if self.mscDICT[message.author.id]['product'] and ('feature' not in resultDICT and "way_pay" not in resultDICT and "benefit" not in resultDICT and "acc_benefit" not in resultDICT and "life_period" not in resultDICT and "no_offer" not in resultDICT):
                        if self.mscDICT[message.author.id]['type']:
                            if ("life" in self.mscDICT[message.author.id]['type'] and len(self.mscDICT[message.author.id]['product']) >= 1) or ("travel" in self.mscDICT[message.author.id]['type'] and len(self.mscDICT[message.author.id]['product']) >= 1)or ("accident" in self.mscDICT[message.author.id]['type'] and len(self.mscDICT[message.author.id]['product']) == 1):
                                print('已有產品且不問追加問題，新的template')
                                age_keep = self.mscDICT[message.author.id]['age']
                                self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                                self.mscDICT[message.author.id] = record_to_discord(resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                self.mscDICT[message.author.id]['age'] = age_keep
                                print(self.mscDICT[message.author.id])
                                
                    

                    # 關鍵字補資訊(地點)
                    if check_place(msgSTR) and check_place(msgSTR) != self.mscDICT[message.author.id]['place']:
                        self.mscDICT[message.author.id]['place'] = check_place(msgSTR) 

                             
                    # 關鍵字打招呼 + 回收抓不到的句子
                    if len(resultDICT) == 1 and not resultDICT['type']:
                        if msgSTR.lower() in 'bye,bye bye,byebye,good bye,拜拜,拜咿,掰掰,那掰掰,沒有問題,沒,沒問題,沒有'.split(','):
                            #刪除之前的對話，並給予結束的回覆。
                            self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                            replySTR = '拜拜，我們下次見囉！☺️✨(若是有其他新的需求，都可以再直接與小Bot聯絡😎)'
                        elif any(greet in msgSTR.lower() for greet in '很棒,很讚,謝謝你,給你五顆星,真讚,真棒,好讚,好棒,感謝,感激,謝謝'.split(',')):
                            replySTR = "謝謝指教，希望有幫到你呦～🥰😳(若是有其他新的需求，都可以再直接與小Bot聯絡😎)" 
                        
                        else:
                            # 抓不到東西
                            print("沒有intent的句子")
                            with open('未在intent.txt', 'a') as f:
                                f.write(msgSTR)
                                f.write("\n")
                            replySTR = '''目前的問題，不涵蓋在小bot的業務範圍或是為**待開發項目**～～💁🏻‍♀️✨\n如果需要其他關於「意外險、旅平險、壽險」的方案推薦，可以根據上面圖片給出資訊喔~~\n\n但若是您沒有其他需求可以直接跟小bot說byebye結束🤖🤖👋👋'''
                            pic2 = discord.File(random.choice(['picture/how_pic.png', 'picture/how_pic2.png']))
                            await message.reply(file = pic2)                               

            
                    else: # 有隸屬的 intent
                        # 沒有抓到特定保險
                        if not self.mscDICT[message.author.id]['type']:
                            print("no_precise_insur")
                            if check_dict_values(self.mscDICT[message.author.id]):
                                replySTR = "{msgSTR.title()}！！   **{message.author}**😆可以根據以上圖片只是告訴我你需要什麼呦！"
                                pic = discord.File("picture/intro_pic.png")
                                await message.reply(file = pic)

                            # 更改年齡
                            elif self.mscDICT[message.author.id]['age'] and "age_change" in self.mscDICT[message.author.id]:
                                del self.mscDICT[message.author.id]["age_change"]
                                replySTR = f"您好呀～～～✨看到您更改了年齡為 **{self.mscDICT[message.author.id]['age'][0]}歲**，為了協助您找到適合的保險以及方案: \n我們提供「意外險、旅平險、壽險」的方案推薦，可以直接敘述需求就好了喔~\n\n【範例】：\n1. 單一資訊：我想保意外險\n2. 多樣資訊：想去日本玩5天\n\n單一資訊可以依據提示內容，回答補充需要的資訊。而多樣資訊則是根據您的不同資訊，直接提供方案。（但如果訊息有所缺漏，也會請您再提供～）"

                            # 幫別人問 ver2
                            elif self.mscDICT[message.author.id]['person'] and "person_change" in self.mscDICT[message.author.id]:
                                del self.mscDICT[message.author.id]["person_change"]
                                if self.mscDICT[message.author.id]['age']:
                                    replySTR = f"ok! 目前的資訊是您的**{self.mscDICT[message.author.id]['person'][0]}**，現在是**{self.mscDICT[message.author.id]['age'][0]}歲**\n那你想要幫他問哪一個險呢？**【意外險、旅平險、壽險】**💁‍♀️"
                                elif not self.mscDICT[message.author.id]['age']:
                                    if self.mscDICT[message.author.id]['person'] == '朋友':        
                                        replySTR = "看來您是想要幫您的**朋友**詢問保險～❤️\n那你想要問哪一個險呢？**【意外險、旅平險、壽險】**💁‍♀️"
                                    else:
                                        replySTR = f"看來您是想要幫您的**{self.mscDICT[message.author.id]['person'][0]}**詢問保險～❤️\n那你想要問哪一個險呢？**【意外險、旅平險、壽險】**💁‍♀️"
                            


                            # 幫別人問
                            elif self.mscDICT[message.author.id]['change']:
                                self.mscDICT[message.author.id]['type'] = []
                                replySTR = "看起來您是想要幫別人問保險～那你想要問什麼的險種**【意外險、旅平險、壽險】**呢？" 

                            # 不會問的提示
                            elif self.mscDICT[message.author.id]['strange']:
                                if "job" in self.mscDICT[message.author.id]['strange']:
                                    replySTR = "若您不知道要如何填寫 **職業** 的話，我們這邊就當您有**職業上的考量**來幫您篩選方案🥰"
                                    if type(self.mscDICT[message.author.id]['acc_con']) == list:
                                        self.mscDICT[message.author.id]['acc_con'].append("job")
                                    else:
                                        self.mscDICT[message.author.id]['acc_con'] = []
                                        self.mscDICT[message.author.id]['acc_con'].append("job")
                                elif "place" in self.mscDICT[message.author.id]['strange']:
                                    replySTR = "若您不知道要如何填寫 **詳細地點** 的話，那請您填入 **國內/國外** 來協助篩選方案喔～🥰"
                                    
                                elif "age" in self.mscDICT[message.author.id]['strange']:
                                    replySTR = "若您不知道被保險人的 **歲數** 的話，那我們這邊會先代入已成年的 **25歲** 來協助篩選方案喔～(取方案中間值)🥰"
                                    self.mscDICT[message.author.id]['age'] = ["25"]
                                    
                                else:
                                    replySTR = f"你好呀～**{message.author}**😆 如果不知道怎麼開始的話，您可以根據以上圖示給出資訊喔～"
                                    self.mscDICT[message.author.id]['strange'] = None 
                                    pic2 = discord.File(random.choice(['picture/how_pic.png', 'picture/how_pic2.png']))
                                    await message.reply(file = pic2)

                            # 確定沒有處理的業務
                            elif self.mscDICT[message.author.id]['no_offer']:
                                replySTR = no_offer(self.mscDICT[message.author.id])
                                self.mscDICT[message.author.id]['no_offer'] = None

                            # 換別的保險
                            elif self.mscDICT[message.author.id]['switch_insur']:
                                replySTR = "看起來您是想要換一個險問～那你想要問什麼的險種**【意外險、旅平險、壽險】**呢？"
                                self.mscDICT[message.author.id]['switch_insur'] = None

                            
                            # 當提供一些條件(在各個保險裡面共有的：如便宜等)
                            elif reply_single_con(self.mscDICT[message.author.id]):
                                condition = reply_single_con(self.mscDICT[message.author.id])
                                if "weak" in condition:
                                    replySTR = "好的！看起來您是**特殊身份**，可以針對您的情況推薦合適的方案！再麻煩您跟我們說你想要哪一個險種**【意外險、壽險】**喔🥴\n這兩種的差別為意外險的話「只保障非疾病的意外」，然後壽險則是沒有這個限制不過還是要看你想要保什麼方案這樣～"
                                elif "high_identity" in condition:
                                    replySTR = "看起來**家庭**應該也是您的考量因素之一，再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔😸"
                                elif "low_identity" in condition:
                                    replySTR = "看起來您目前的狀態或身份需要一個比較**小資且價格實惠**的方案，那再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔💁🏻‍♀️"
                                elif "job" in condition:
                                    replySTR = "謝謝您告訴我您的**職業**喔～那再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔🥴"                              
                                elif "high" in condition and "low" in condition:
                                    replySTR = "好的！看起來您應該是想要**「高保障低保費」**的保險對吧～那再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔💁🏻‍♀️"
                                elif "high" in condition:
                                    replySTR = "好的！看起來您想要**「保障多或加倍保障」**的保險！再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔🥴"
                                elif "low" in condition:
                                    replySTR = "好的！看起來您想要**「省錢、價格實惠或基礎」**的保險！再麻煩您跟我們說你想要哪一個險種**【意外險、旅平險、壽險】**喔🥴"


                            # 特定險的獨家特色
                            # 定期終身
                            elif self.mscDICT[message.author.id]['life_period']:
                                # new   
                                self.mscDICT[message.author.id] = life_period(self.mscDICT[message.author.id])                           
                                replySTR = self.mscDICT[message.author.id]['temp_ans']
                                del self.mscDICT[message.author.id]['temp_ans']    
                                self.mscDICT[message.author.id]['life_period'] = None
                            elif self.mscDICT[message.author.id]['acc_benefit']:
                                # new
                                self.mscDICT[message.author.id] = acc_benefit(self.mscDICT[message.author.id])                           
                                replySTR = self.mscDICT[message.author.id]['temp_ans']
                                del self.mscDICT[message.author.id]['temp_ans']
                                self.mscDICT[message.author.id]['acc_benefit'] = None

                                

                            # 追加問題(特色、支付方式、給付項目)
                            elif self.mscDICT[message.author.id]['feature']:
                                replySTR = "那你想要問什麼的險種**【意外險、旅平險、壽險】**的特色呢～😎😎"
                            elif self.mscDICT[message.author.id]['way_pay']:
                                replySTR = "那你想要問什麼的險種**【意外險、旅平險、壽險】**的支付方式呢～😎😎"
                            elif self.mscDICT[message.author.id]['benefit']:
                                replySTR = "那你想要問什麼的險種**【意外險、旅平險、壽險】**的給付項目呢～😎😎"


                            elif self.mscDICT[message.author.id]['age']:
                                replySTR = f"好的，您的年齡為{self.mscDICT[message.author.id]['age'][0]}歲，為了幫助您: \n我們提供「意外險、旅平險、壽險」的方案推薦，可以直接敘述需求就好了喔~\n\n【範例】：\n1. 單一資訊：我想保意外險 \n2. 多樣資訊：想去日本玩5天\n\n單一資訊可以依據提示內容，回答補充需要的資訊。而多樣資訊則是根據您的不同資訊，直接提供方案。（但如果訊息有所缺漏，也會請您再提供～）"



                        # 有抓到保險
                        elif self.mscDICT[message.author.id]['type']:
                            # 確定沒有處理的業務
                            if self.mscDICT[message.author.id]['no_offer']:
                                replySTR = no_offer(self.mscDICT[message.author.id])
                                self.mscDICT[message.author.id]['no_offer'] = None
                            # # 換別的保險
                            elif self.mscDICT[message.author.id]['switch_insur']:
                                replySTR = "看起來您是想要**換一個保險**問～那你想要問什麼的險種**【意外險、旅平險、壽險】**呢？"
                                self.mscDICT[message.author.id]['switch_insur'] = None


                            elif len(self.mscDICT[message.author.id]['type']) == 1:
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    replySTR = travel_response(message.author, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))                   
                                    print("travel:", self.mscDICT[message.author.id])
                                    
                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    replySTR = life_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    print("life:", self.mscDICT[message.author.id])

                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    replySTR = accident_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    print("accident:", self.mscDICT[message.author.id])

                                
                                

                                

                            # 同時多種險種
                            elif len(self.mscDICT[message.author.id]['type']) > 1:
                                replySTR = "看起來您可能想要同時保好幾個險，或許您可以一個個來，以便我們幫您推薦最適合您的方案喔！💁🏻‍♀️請問想先問哪個險**(意外險/壽險/旅平險)**呢？"



                            # 追加疑問
                            # 支付方式
                            if self.mscDICT[message.author.id]['way_pay']:
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    replySTR = travel_pay(self.mscDICT[message.author.id]['way_pay'][0])
                                    self.mscDICT[message.author.id]['way_pay'] = None

                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    replySTR = life_pay(self.mscDICT[message.author.id]['way_pay'][0])
                                    self.mscDICT[message.author.id]['way_pay'] = None

                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    replySTR = acc_pay(self.mscDICT[message.author.id]['way_pay'][0])
                                    self.mscDICT[message.author.id]['way_pay'] = None
                            # 給付項目         
                            elif self.mscDICT[message.author.id]['benefit']:
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    replySTR = travel_comp(self.mscDICT[message.author.id]['benefit'])
                                    self.mscDICT[message.author.id]['benefit'] = None

                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    replySTR = life_comp(resultDICT,  self.mscDICT[message.author.id])
                                    self.mscDICT[message.author.id]['benefit'] = None

                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    replySTR = acc_comp(self.mscDICT[message.author.id])
                                    self.mscDICT[message.author.id]['benefit'] = None
                            # 特色
                            elif self.mscDICT[message.author.id]['feature']:
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    if not self.mscDICT[message.author.id]['product']:
                                        self.mscDICT[message.author.id]['product'] = ['旅平險']
                                    replySTR = feature_insur(self.mscDICT[message.author.id])
                                    self.mscDICT[message.author.id]['feature'] = None
                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    if not self.mscDICT[message.author.id]['product']:
                                        self.mscDICT[message.author.id]['product'] = ['壽險']
                                    replySTR = feature_insur(self.mscDICT[message.author.id])
                                    self.mscDICT[message.author.id]['feature'] = None
                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    if not self.mscDICT[message.author.id]['product']:
                                        self.mscDICT[message.author.id]['product'] = ['意外險']
                                    replySTR = feature_insur(self.mscDICT[message.author.id])
                                    self.mscDICT[message.author.id]['feature'] = None
                            

                            # 特定險的獨家特色
                            # 定期終身
                            elif self.mscDICT[message.author.id]['life_period']:
                                self.mscDICT[message.author.id] = life_period(self.mscDICT[message.author.id])                           
                                replySTR = self.mscDICT[message.author.id]['temp_ans']
                                del self.mscDICT[message.author.id]['temp_ans']
                                
                                self.mscDICT[message.author.id]['life_period'] = None
                            
                            # 實支實付、骨折等
                            elif self.mscDICT[message.author.id]['acc_benefit']:
                                self.mscDICT[message.author.id] = acc_benefit(self.mscDICT[message.author.id])                           
                                replySTR = self.mscDICT[message.author.id]['temp_ans']
                                del self.mscDICT[message.author.id]['temp_ans']                            

                            # 幫別人問
                            if self.mscDICT[message.author.id]['change']:
                                print('幫別人問  ', self.mscDICT[message.author.id])
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    replySTR = "**看起來您是想要幫別人問保險～**\n\n" + travel_response(message.author, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    self.mscDICT[message.author.id]['change'] = None
                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    replySTR = "**看起來您是想要幫別人問保險～**\n\n" + life_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    self.mscDICT[message.author.id]['change'] = None                               
                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    replySTR = "**看起來您是想要幫別人問保險～**\n\n" + accident_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    self.mscDICT[message.author.id]['change'] = None

                            # 幫別人問 ver2
                            if self.mscDICT[message.author.id]['person'] and "person_change" in self.mscDICT[message.author.id]:
                                del self.mscDICT[message.author.id]["person_change"]
                                if "travel" in self.mscDICT[message.author.id]['type']:
                                    if self.mscDICT[message.author.id]['person'] == '朋友':        
                                        replySTR = "看來您是想要幫您的**朋友**詢問保險～❤️\n\n" + travel_response(message.author, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    else:
                                        replySTR = f"看來您是想要幫您的**{self.mscDICT[message.author.id]['person'][0]}**詢問保險～❤️\n\n"+ travel_response(message.author, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                elif "life" in self.mscDICT[message.author.id]['type']:
                                    if self.mscDICT[message.author.id]['person'] == '朋友':   
                                    
                                        replySTR = "看來您是想要幫您的**朋友**詢問保險～❤️\n\n" + life_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    else:
                                        replySTR = f"看來您是想要幫您的**{self.mscDICT[message.author.id]['person'][0]}**詢問保險～❤️\n\n" + life_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))

                                elif "accident" in self.mscDICT[message.author.id]['type']:
                                    if self.mscDICT[message.author.id]['person'] == '朋友':                                 
                                        replySTR = "**看起來您是想要幫別人問保險～**\n\n" + accident_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))
                                    else:
                                        replySTR = f"看來您是想要幫您的**{self.mscDICT[message.author.id]['person'][0]}**詢問保險～❤️\n\n" + accident_response(message.author, resultDICT, self.mscDICT[message.author.id], self.resetMSCwith(message.author.id))


            await message.reply(replySTR)
            
                         
            


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
