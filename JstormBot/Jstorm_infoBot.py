# -*- coding:utf-8 -*-

import logging
import datetime
import discord
import json
import math
import re
from pprint import pprint

from Jstorm2 import runLoki
logging.basicConfig(level=logging.INFO)


DISCORD_TOKEN=""


# <取得多輪對話資訊>
client = discord.Client()

requestTemplate ={"group":"",
                 "member": "",
                 "request": "",}

mscDICT = {# "userID": {requestTemplate}
           }
# </取得多輪對話資訊>



    
# 另一個寫法是：accountDICT = json.load(open("account.info", encoding="utf-8"))
with open('D:\HAO\Hao的研所\實習\LokiHub\JstormBot\web_crawler\ProfileDICT.json', 'r') as f:
    ProfileDICT=json.load(f)
with open('D:\HAO\Hao的研所\實習\LokiHub\JstormBot\web_crawler\GroupDICT.json', 'r') as f:
    GroupDICT=json.load(f)

tokio=['国分太一','城島茂','松岡昌宏']
arashi=['相葉雅紀','松本潤','二宮和也','大野智','櫻井翔']
kattun=['亀梨和也','上田竜也','中丸雄一']
jump=['山田涼介','知念侑李','中島裕翔','有岡大貴','髙木雄也','伊野尾慧','八乙女光','薮宏太']

ageDICT={"TOKIO":['城島茂','国分太一','松岡昌宏'],
         "嵐":['大野智','櫻井翔','相葉雅紀','二宮和也','松本潤'],
         "KAT-TUN":['中丸雄一','上田竜也','亀梨和也'],
         "Hey! Say! JUMP":['薮宏太','髙木雄也','伊野尾慧','八乙女光','有岡大貴','山田涼介','中島裕翔','知念侑李']}


punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    print("Loki Result => {}".format(resultDICT))
    return resultDICT

def findAge(name): #計算歲數
    '''
    輸入：全名
    輸出：歲數(int)
    '''
    if name in tokio:
        for n in range(0,len(ProfileDICT['TOKIO'])):
         if ProfileDICT['TOKIO'][n]['JName']==name:
             birth=ProfileDICT['TOKIO'][n]['Birth'].split(".")
    if name in arashi:
        for n in range(0,len(ProfileDICT['嵐'])):
         if ProfileDICT['嵐'][n]['JName']==name:
             birth=ProfileDICT['嵐'][n]['Birth'].split(".")
    if name in kattun:
        for n in range(0,len(ProfileDICT['KAT-TUN'])):
         if ProfileDICT['KAT-TUN'][n]['JName']==name:
             birth=ProfileDICT['KAT-TUN'][n]['Birth'].split(".")
    if name in jump:
        for n in range(0,len(ProfileDICT['Hey! Say! JUMP'])):
         if ProfileDICT['Hey! Say! JUMP'][n]['JName']==name:
             birth=ProfileDICT['Hey! Say! JUMP'][n]['Birth'].split(".")
    
    birthday=datetime.date(year=int(birth[0]),month=int(birth[1]),day=int(birth[2]))
    today=datetime.date.today()
    age= math.floor((today-birthday).days/365)
    
    return age

def findBlood(group,blood):
    '''
    輸入:團名,血型
    輸出:人名
    '''
    bloodLIST=[]
    for n in range(0,len(ProfileDICT[group])):
        if ProfileDICT[group][n]['Blood'] == blood:
            bloodLIST.append(ProfileDICT[group][n]['JName'])
        else:
            bloodLIST.append('no')
            
    nameLIST=[]
    for e in bloodLIST:
        if e != 'no':
            nameLIST.append(e)
    
    if nameLIST==[]:
        nameLIST='no'

    return nameLIST

def findHeight(name):
    '''
    輸入：全名
    輸出：身高(int)
    '''
    if name in tokio:
        for n in range(len(ProfileDICT["TOKIO"])):
           if name == ProfileDICT["TOKIO"][n]['JName']:
               height=ProfileDICT["TOKIO"][n]['height']
    if name in arashi:
         for n in range(len(ProfileDICT["嵐"])):
            if name == ProfileDICT["嵐"][n]['JName']:
                height=ProfileDICT["嵐"][n]['height']                             
    if name in kattun:
         for n in range(len(ProfileDICT["KAT-TUN"])):
            if name == ProfileDICT["KAT-TUN"][n]['JName']:
                height=ProfileDICT["KAT-TUN"][n]['height']   
    if name in jump:
         for n in range(len(ProfileDICT["Hey! Say! JUMP"])):
            if name == ProfileDICT["Hey! Say! JUMP"][n]['JName']:
                height=ProfileDICT["Hey! Say! JUMP"][n]['height']  
    return height

def findBirthday(name):
    '''
    輸入：全名
    輸出：[年,月,日]
    '''
    birthday=[]
    if name in tokio:
        for n in range(len(tokio)):
            if name==ProfileDICT["TOKIO"][n]["JName"]:
                birthday = ProfileDICT["TOKIO"][n]["Birth"].split(".")
    if name in arashi:
        for n in range(len(arashi)):
            if name==ProfileDICT["嵐"][n]["JName"]:
                birthday = ProfileDICT["嵐"][n]["Birth"].split(".")
    if name in kattun:
        for n in range(len(kattun)):
            if name==ProfileDICT["KAT-TUN"][n]["JName"]:
                birthday = ProfileDICT["KAT-TUN"][n]["Birth"].split(".")
    if name in jump:
        for n in range(len(tokio)):
            if name==ProfileDICT["Hey! Say! JUMP"][n]["JName"]:
                birthday = ProfileDICT["Hey! Say! JUMP"][n]["Birth"]
    return birthday

def findColor(name):
    '''
    輸入:全名
    輸出：顏色(str)
    '''
    if name in tokio:
        index=tokio.index(name)
        color = ProfileDICT['TOKIO'][index]['color']
        
    if name in arashi:
        index=arashi.index(name)
        color = ProfileDICT['嵐'][index]['color']
        
    if name in kattun:
        index=kattun.index(name)
        color = ProfileDICT['KAT-TUN'][index]['color']
        
    if name in jump:
        index=jump.index(name)
        color = ProfileDICT['Hey! Say! JUMP'][index]['color']

    return color

def findColorLIST(group):
    '''
    輸入：團名
    輸出：顏色(list)
    '''
    colorLIST=[]
    if group=='TOKIO':
        for n in range(len(tokio)):
            colorLIST.append(ProfileDICT['TOKIO'][n]['color'])                 
    if group=='嵐':
        for n in range(len(arashi)):
            colorLIST.append(ProfileDICT['嵐'][n]['color'])                            
    if group=='KAT-TUN':
        for n in range(len(kattun)):
            colorLIST.append(ProfileDICT['KAT-TUN'][n]['color'])                              
    if group=='Hey! Say! JUMP':
        for n in range(len(jump)):
            colorLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['color'])
    return colorLIST

def findDate(group,anniversary):
    '''
    輸入:團名,'formationdate'/'debutdate'
    輸出：日期(str)
    '''
    if anniversary=='formationdate':
        if group=='TOKIO':
            date=GroupDICT['TOKIO']['formationdate']
        if group=='嵐':
            date=GroupDICT['嵐']['formationdate']                 
        if group=='KAT-TUN':
            date=GroupDICT['KAT-TUN']['formationdate']                 
        if group=='Hey! Say! JUMP':
            date=GroupDICT['Hey! Say! JUMP']['formationdate']
    elif anniversary=='debutdate':
        if group=='TOKIO':
            date=GroupDICT['TOKIO']['debutdate']
        if group=='嵐':
            date=GroupDICT['嵐']['debutdate']                     
        if group=='KAT-TUN':
            date=GroupDICT['KAT-TUN']['debutdate']                
        if group=='Hey! Say! JUMP':
            date=GroupDICT['Hey! Say! JUMP']['debutdate']            
    return date

def findInfo(name):
    '''
    輸入：本名
    輸出：[日文名字,英文名字,圖片,生日,血型,身高,出生地,成員色](list)
    '''
    infoLIST=[]
    if name in tokio:
        for n in range(len(tokio)):
            if ProfileDICT['TOKIO'][n]['JName']==name:
                infoLIST.append(ProfileDICT['TOKIO'][n]['JName'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['EName'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['Pic'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['Birth'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['Blood'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['height'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['Born'])
                infoLIST.append(ProfileDICT['TOKIO'][n]['color'])
                
    if name in arashi:
        for n in range(len(arashi)):         
            if ProfileDICT['嵐'][n]['JName']==name:
                infoLIST.append(ProfileDICT['嵐'][n]['JName'])
                infoLIST.append(ProfileDICT['嵐'][n]['EName'])
                infoLIST.append(ProfileDICT['嵐'][n]['Pic'])
                infoLIST.append(ProfileDICT['嵐'][n]['Birth'])
                infoLIST.append(ProfileDICT['嵐'][n]['Blood'])
                infoLIST.append(str(ProfileDICT['嵐'][n]['height']))
                infoLIST.append(ProfileDICT['嵐'][n]['Born'])
                infoLIST.append(ProfileDICT['嵐'][n]['color'])
                
    if name in kattun:
        for n in range(len(kattun)):
            if ProfileDICT['KAT-TUN'][n]['JName']==name:
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['JName'])
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['EName'])
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['Pic'])
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['Birth'])
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['Blood'])
                infoLIST.append(str(ProfileDICT['KAT-TUN'][n]['height']))
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['Born'])
                infoLIST.append(ProfileDICT['KAT-TUN'][n]['color'])
            
    if name in jump:
        for n in range(len(jump)):
            if ProfileDICT['Hey! Say! JUMP'][n]['JName']==name:
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['JName'])
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['EName'])
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['Pic'])
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['Birth'])
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['Blood'])
                infoLIST.append(str(ProfileDICT['Hey! Say! JUMP'][n]['height']))
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['Born'])
                infoLIST.append(ProfileDICT['Hey! Say! JUMP'][n]['color'])

    return infoLIST

def countDays(group,anniversary):
    '''
    輸入:團名,'formationdate'/'debutdate'
    輸出:距離下一次節日的天數(int)
    '''
    if anniversary == 'formationdate':
        if group == 'TOKIO':
            date=GroupDICT[group]['formationdate'].split('.')
            date.append('1')
        elif group == '嵐':
            date=GroupDICT[group]['formationdate'].split('.')
        elif group == 'KAT-TUN':
            date=GroupDICT[group]['formationdate'].split('.')
        elif group == 'Hey! Say! JUMP':
            date=GroupDICT[group]['formationdate'].split('.')

    elif anniversary == 'debutdate':
        if group == 'TOKIO':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == '嵐':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == 'KAT-TUN':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == 'Hey! Say! JUMP':
            date=GroupDICT[group]['debutdate'].split('.')
    
    today=datetime.date.today()
    current_anniversary= datetime.date(year=today.year, month=int(date[1]),day=int(date[2]))
 
    if current_anniversary<today:
        if today.year/4 != 0:
            days=(current_anniversary-today).days+365
        else:
            days=(current_anniversary-today).days+366
    else: #current_birthday>today
        days=(current_anniversary-today).days

    return days

def countYears(group,anniversary):
    '''
    輸入:團名,'formationdate'/'debutdate'
    輸出:年(int)
    '''
    if anniversary == 'formationdate':
        if group == 'TOKIO':
            date=GroupDICT[group]['formationdate'].split('.')
        elif group == '嵐':
            date=GroupDICT[group]['formationdate'].split('.')
        elif group == 'KAT-TUN':
            date=GroupDICT[group]['formationdate'].split('.')
        elif group == 'Hey! Say! JUMP':
            date=GroupDICT[group]['formationdate'].split('.')

    elif anniversary == 'debutdate':
        if group == 'TOKIO':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == '嵐':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == 'KAT-TUN':
            date=GroupDICT[group]['debutdate'].split('.')
        elif group == 'Hey! Say! JUMP':
            date=GroupDICT[group]['debutdate'].split('.')
    

    this_year=datetime.date.today().year
    anniversary_year=int(date[0])
 
    years=this_year-anniversary_year

    return years

def maxIndex(list): #找最大值的index
    index=[]
    maxOne=max(list)
    for i in range(len(list)):
        if list[i] == maxOne:
            index.append(i)
    return index

def minIndex(list): #找最小值的index
    index=[]
    minOne=min(list)
    for i in range(len(list)):
        if list[i] == minOne:
            index.append(i)
    return index

@client.event
async def on_ready():
    logging.info("[READY INFO] {} has connected to Discord!".format(client.user))
    print("[READY INFO] {} has connected to Discord!".format(client.user))


@client.event
async def on_message(message):
    if not re.search("<@[!&]{}> ?".format(client.user.id), message.content):    # 只有 @Bot 才會回應
        return

    if message.author == client.user:
        return

    # Greetings
    print("client.user.id =", client.user.id, "\nmessage.content =", message.content)
    msgSTR = re.sub("<@[!&]{}> ?".format(client.user.id), "", message.content)    # 收到 User 的訊息，將 id 取代成 ""
    logging.info(msgSTR)
    #print("msgSTR =", msgSTR)
    replySTR = ""    # Bot 回應訊息

    if msgSTR in ("","哈囉","嗨","嗨嗨","你好","您好","在嗎","早安","午安","晚安","こんにちは","こんばんは","やっほー","やっはろ","やほー","Hi","hi","hello","Hello","安安"):
        replySTR = "你好呀~有什麼可以為你服務的？\n我可以提供你Jstorm旗下藝人的基本資料喔！\n（團體的基本資料、各團成員的基本資料）"
        await message.reply(replySTR)

    else:
        lokiResultDICT=getLokiResult(msgSTR)    # 取得 Loki 回傳結果
        print(lokiResultDICT)
        
        if client.user.id not in mscDICT:    # 判斷 User 是否為第一輪對話
            mscDICT[client.user.id] = {"group":"",
                                       "member":"",
                                       "request":"",
                                       "completed": False,
                                       "updatetime": datetime.datetime.now()}
         
        # 處理時間差
        datetimeNow = datetime.datetime.now()  # 取得當下時間
        timeDIFF = datetimeNow - mscDICT[client.user.id]["updatetime"]
        if timeDIFF.total_seconds() <= 300:    # 以秒為單位，5分鐘以內都算是舊對話
            mscDICT[client.user.id]["updatetime"] = datetimeNow    
        
        #如果member是list，換Group或是換request時清空member
        if len(lokiResultDICT.keys()) == 1 and type(mscDICT[client.user.id]["member"])==list:
            mscDICT[client.user.id]["member"] = ""
            
        #多輪對話
        if lokiResultDICT:
            for k in lokiResultDICT.keys():    # 將 Loki Intent 的結果，存進 Global mscDICT 變數，可替換成 Database。
                if k == "Group":
                    mscDICT[client.user.id]["group"] = lokiResultDICT["Group"]
                elif k == "member":
                    mscDICT[client.user.id]["member"] = lokiResultDICT["member"]
                elif k == 'request':
                    mscDICT[client.user.id]["request"] = lokiResultDICT["request"]
    

        print("mscDICT =")
        pprint(mscDICT)
 
        if mscDICT[client.user.id]["request"] == "":  # 多輪對話的問句。
            replySTR = '請問你想問的是哪方面呢？\n（基本資料、日英姓名、生日、年齡、血型、身高、出身地、成員色）'
        
        elif mscDICT[client.user.id]['group'] == "" and mscDICT[client.user.id]["member"] == "": 
            if mscDICT[client.user.id]["request"] in ("age","height","birth",'year','month','day','color'):
                replySTR = "請問您是問哪一個團體的哪位成員呢？"   
            elif mscDICT[client.user.id]["request"] in ("formationdate","debutdate","formationdate.years","debutdate.years","formationdate.days","debutdate.days","age.max","age.min","age.sort.HtoL","age.sort.LtoH","height.max","height.min","height.sort.HtoL","height.sort.LtoH"):
                replySTR = "請問您是問哪一個團體的呢？"
        
        elif mscDICT[client.user.id]["group"]=="":
            replySTR = "請問您是問哪一個團體呢？"
        
        elif mscDICT[client.user.id]["member"] == "" and mscDICT[client.user.id]["request"] in ("age","height","birth",'year','month','day','color'):
            replySTR = "請問您是問哪一位成員呢？"
            
        else:  #給答案
         
            #Group
            if type(mscDICT[client.user.id]["group"])==list and mscDICT[client.user.id]["member"] =="":
                if type(mscDICT[client.user.id]["request"]) == int:
                    replySTR = '共有 '+str(mscDICT[client.user.id]["request"])+' 團。'
                else:
                    answerSTR=""
                    for n in range(0,len(lokiResultDICT['Group'])):
                        answerSTR+=lokiResultDICT['Group'][n]+lokiResultDICT['request'][lokiResultDICT['Group'][n]]+'\n'
    
                    replySTR = "有以下團體：\n"+answerSTR
                    
            elif type(mscDICT[client.user.id]["group"])==str and mscDICT[client.user.id]["request"] in ('yes','no'):
                if mscDICT[client.user.id]["request"]=='yes':
                    replySTR = '沒錯，正是如此。'
                else: 
                    replySTR = mscDICT[client.user.id]["group"]+' 並不是Jstorm旗下的團體。'
            
            
            #member
            elif type(mscDICT[client.user.id]["member"])==list:
                if type(mscDICT[client.user.id]["request"])==list:
                    for e in mscDICT[client.user.id]["request"]:
                        if e in ("A型","B型","O型","AB型"):  #問各血型
                            answerSTR=""
                            for n in range(len(mscDICT[client.user.id]["member"])):
                                answerSTR+=lokiResultDICT['member'][n]+' 是 '+lokiResultDICT['request'][n]+'。\n'
                            replySTR = answerSTR
                            
                        
                        else:  #問整團成員
                            answerSTR=""
                            for n in range(len(mscDICT[client.user.id]["member"])):
                                answerSTR+=lokiResultDICT['member'][n]+lokiResultDICT['request'][n]+'\n'
                            replySTR = "有以下成員：\n"+answerSTR
                            
                    
                    
                else: #type(mscDICT[client.user.id]["request"])!=list   
                    if len(mscDICT[client.user.id]["request"])>2:#問特定出生地
                        answerSTR=""
                        for n in range(len(mscDICT[client.user.id]["member"])):
                            answerSTR+=lokiResultDICT['member'][n]+" "
                        replySTR =answerSTR+"來自 "+mscDICT[client.user.id]["request"]+"。"
                        
                    else: #問特定血型
                        answerSTR=""
                        for n in range(len(mscDICT[client.user.id]["member"])):
                            answerSTR+=lokiResultDICT['member'][n]+" "
                        replySTR =answerSTR+"是 "+mscDICT[client.user.id]["request"]+"。"
                        
                    
            
            elif type(mscDICT[client.user.id]["member"])==str:
                if mscDICT[client.user.id]["request"] == 'yes': #成員和團體有對上
                    replySTR='沒錯，正是如此。'
                          
                elif mscDICT[client.user.id]["request"] == 'no': #成員和團體沒對上
                    replySTR=f'不， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                
                elif mscDICT[client.user.id]["request"] == 'weight': #問體重
                    replySTR="怎麼可以問人家體重呢> <"
                    
                elif mscDICT[client.user.id]["request"] == 'personalinfo': #問個人資訊
                     info=findInfo(mscDICT[client.user.id]["member"])   
                     replySTR=f'''日文姓名：{info[0]}
英文姓名：{info[1]}
生日：{info[3]}
血型：{info[4]}
身高：{info[5]}cm
出生地：{info[6]}
成員色：{info[7]}色
{info[2]} '''

                    
                #anniversary
                elif mscDICT[client.user.id]["request"] in ('formationdate','debutdate','formationdate,years','formationdate.days','debutdate.years','debutdate.days'):
                    if mscDICT[client.user.id]["request"]=='formationdate':#結成日
                        date=findDate(mscDICT[client.user.id]["group"],'formationdate')
                        if mscDICT[client.user.id]["group"] == 'TOKIO':
                            replySTR="他們的結成日是 "+ date[:4]+"年 "+date[5:6]+"月。"
                        else:
                            replySTR="他們的結成日是 "+ date +"。"
                    elif mscDICT[client.user.id]["request"]=='debutdate':#出道日
                        date=findDate(mscDICT[client.user.id]["group"],'debutdate')
                        replySTR="他們的出道日是 "+ date +"。"
                        
                    elif mscDICT[client.user.id]["request"]=='formationdate.years': #出道幾年
                        years=countYears(mscDICT[client.user.id]["group"],'formationdate')
                        replySTR="他們已經結成 "+ str(years) +"年了。"
                            
                    elif mscDICT[client.user.id]["request"]=='debutdate.years': #出道幾年
                        years=countYears(mscDICT[client.user.id]["group"],'debutdate')
                        replySTR="他們已經出道 "+ str(years) +"年了。"
                        
                    elif mscDICT[client.user.id]["request"]=='formationdate.days': #出道幾年
                        days=countDays(mscDICT[client.user.id]["group"],'formationdate')
                        replySTR="離結成日還有 "+ str(days) +"天。"
                        
                    elif mscDICT[client.user.id]["request"]=='debutdate.days': #出道幾年
                        days=countDays(mscDICT[client.user.id]["group"],'debutdate')
                        replySTR="離出道日還有 "+ str(days) +"天。"
                        
                #color
                elif mscDICT[client.user.id]["request"] in ('color','color.list'):
                    if mscDICT[client.user.id]["request"] == 'color': #問顏色
                        color = findColor(mscDICT[client.user.id]["member"])
                        replySTR=mscDICT[client.user.id]["member"]+' 的成員色是 '+color+'色。'
                    elif mscDICT[client.user.id]["request"] == 'color.list': #問總共有什麼顏色
                        colorLIST=findColorLIST(mscDICT[client.user.id]["group"])
                        answerSTR=""
                        if mscDICT[client.user.id]["group"] == 'TOKIO':
                            for n in range(len(colorLIST)):
                                answerSTR += tokio[n]+' 的成員色是 '+colorLIST[n]+'色。\n' 
                        if mscDICT[client.user.id]["group"] == '嵐':
                            for n in range(len(colorLIST)):
                                answerSTR += arashi[n]+' 的成員色是 '+colorLIST[n]+'色。\n'                            
                        if mscDICT[client.user.id]["group"] == 'KAT-TUN':
                            for n in range(len(colorLIST)):
                                answerSTR += kattun[n]+' 的成員色是 '+colorLIST[n]+'色。\n'                          
                        if mscDICT[client.user.id]["group"] == 'Hey! Say! JUMP':
                            for n in range(len(colorLIST)):
                                answerSTR += jump[n]+' 的成員色是 '+colorLIST[n]+'色。\n'
                        
                        replySTR=answerSTR
                
                elif mscDICT[client.user.id]["request"] in ('紅', '橙', '黃', '綠', '藍', '紫', '天藍', '粉', '粉紅', '黃綠', '淺綠', '草綠', '淡綠'):  
                    #有沒有人是這個顏色
                    if mscDICT[client.user.id]["group"] == 'TOKIO':
                        tokio_color=findColorLIST('TOKIO')
                        if mscDICT[client.user.id]["request"] in tokio_color:
                            index=tokio_color.index(mscDICT[client.user.id]["request"])
                            member=tokio[index]
                            replySTR=member+' 的成員色是 '+mscDICT[client.user.id]["request"]+'色。\n'                    
                    elif mscDICT[client.user.id]["group"] == '嵐':
                        arashi_color=findColorLIST('嵐')
                        if mscDICT[client.user.id]["request"] in arashi_color:
                            index=arashi_color.index(mscDICT[client.user.id]["request"])
                            member=arashi[index]
                            replySTR=member+' 的成員色是 '+mscDICT[client.user.id]["request"]+'色。\n'                         
                    elif mscDICT[client.user.id]["group"] == 'KAT-TUN':
                        kattun_color=findColorLIST('KAT-TUN')
                        if mscDICT[client.user.id]["request"] in kattun_color:
                            index=kattun_color.index(mscDICT[client.user.id]["request"])
                            member=kattun[index]
                            replySTR=member+' 的成員色是 '+mscDICT[client.user.id]["request"]+'色。\n'                       
                    elif mscDICT[client.user.id]["group"] == 'Hey! Say! JUMP':
                        jump_color=findColorLIST('Hey! Say! JUMP')
                        if mscDICT[client.user.id]["request"] in jump_color:
                            index=jump_color.index(mscDICT[client.user.id]["request"])
                            member=jump[index]
                            replySTR=member+' 的成員色是 '+mscDICT[client.user.id]["request"]+'色。\n'
                
                elif mscDICT[client.user.id]["request"] == 'no.color': #沒人是這個顏色
                    replySTR='沒有人的代表色是這個顏色。'
                
                #name
                elif mscDICT[client.user.id]["request"] == 'yes.group': #有這個人
                    replySTR=f'有的， {mscDICT[client.user.id]["member"]} 是 {mscDICT[client.user.id]["group"]} 的成員。'
                    
                elif mscDICT[client.user.id]["request"] == 'no.group': #沒這個人
                    replySTR=f'{mscDICT[client.user.id]["member"]} 不是Jstorm旗下的人。'
                    
                    
                elif  mscDICT[client.user.id]["request"] in ("JName","EName","JLname","JFname","ELname","EFname"):
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])):
                        if ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']==mscDICT[client.user.id]["member"]:
                            index=n
                    if mscDICT[client.user.id]["request"] == "JName":
                        replySTR= mscDICT[client.user.id]['member']
                        
                    if mscDICT[client.user.id]["request"] == "EName":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EName']
                        
                    if mscDICT[client.user.id]["request"] == "JLname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JLname']
                        
                    if mscDICT[client.user.id]["request"] == "JFname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['JFname']
                        
                    if mscDICT[client.user.id]["request"] == "EFname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['EFname']
                        
                    if mscDICT[client.user.id]["request"] == "ELname":
                        replySTR=ProfileDICT[mscDICT[client.user.id]["group"]][index]['ELname']
                        
                
                #age
                elif mscDICT[client.user.id]["request"] in ("age","age.max","age.min","age.sort.HtoL","age.sort.LtoH"):
                    ageLIST=[]
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])) :
                        ageLIST.append(findAge(ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']))
                        
                    if mscDICT[client.user.id]["request"] == 'age': #回報歲數
                        replySTR=str(findAge(mscDICT[client.user.id]["member"]))+"歲"
                        
                        
                    elif mscDICT[client.user.id]["request"] == 'age.max': #回報最年長
                        indexLIST=maxIndex(ageLIST)
                        if len(indexLIST) != 1:  #如果很多人同歲比較生日
                            birthLIST=[]
                            for i in indexLIST:
                                birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                            index=birthLIST.index(min(birthLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                            
                        else: #len(indexLIST) == 1
                            index=ageLIST.index(max(ageLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                            
                            
                            
                    elif mscDICT[client.user.id]["request"] == 'age.min': #回報最年幼
                        indexLIST=minIndex(ageLIST)
                        if len(indexLIST) != 1: #如果很多人同歲比較生日
                            birthLIST=[]
                            for i in indexLIST:
                                birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                            index=birthLIST.index(max(birthLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName']+f" ，他 {ageLIST[indexLIST[index]]} 歲。"
                            
                        else: #len(indexLIST) == 1
                            index=ageLIST.index(min(ageLIST))
                            replySTR="是 "+ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName']+f" ，他 {ageLIST[index]} 歲。"
                            
                            
                    elif mscDICT[client.user.id]["request"] == 'age.sort.HtoL': #年齡從大排到小
                        groupLIST=ageDICT[mscDICT[client.user.id]["group"]]
                        answerSTR=""
                        for n in range(len(groupLIST)):
                            answerSTR+=groupLIST[n]+' ， '+str(findAge(groupLIST[n]))+' 歲。\n'
                        replySTR='年齡從大排到小為：\n'+answerSTR
                        
    
                    elif mscDICT[client.user.id]["request"] == 'age.sort.LtoH':  #年齡從小排到大
                        ageDICT[mscDICT[client.user.id]["group"]].reverse()
                        groupLIST=ageDICT[mscDICT[client.user.id]["group"]]
                        answerSTR=""
                        for n in range(len(groupLIST)):
                            answerSTR+=groupLIST[n]+' ， '+str(findAge(groupLIST[n]))+' 歲。\n'
                        replySTR='年齡從小排到大為：\n'+answerSTR
                        
                        
                        
                elif mscDICT[client.user.id]["request"] in ("year","month","day"): #問年月日
                    birthday=findBirthday(mscDICT[client.user.id]["member"])
                
                    if mscDICT[client.user.id]["request"] == 'year':
                        replySTR='他是 '+birthday[0]+'年出生的。'
                        
                    elif mscDICT[client.user.id]["request"] == 'month':
                        replySTR='他是 '+birthday[1]+'月出生的。'
                        
                    elif mscDICT[client.user.id]["request"] == 'day':
                        replySTR='他是 '+birthday[2]+'日出生的。'
                        
                        
                       
                elif mscDICT[client.user.id]["request"] in ("height.max","height.min","height.sort.HtoL","height.sort.LtoH"):
                    heightLIST=[]
                    for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])):
                        heightLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])
                        
                    if mscDICT[client.user.id]["request"] =="height": #身高
                        replySTR= mscDICT[client.user.id]["member"]+"，他 "+str(findHeight(mscDICT[client.user.id]["member"]))+" cm。"
                        
                    
                    
                    if mscDICT[client.user.id]["request"] =="height.max":  #最高
                        indexLIST=maxIndex(heightLIST)
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]["JName"]+"，他 "+ str(heightLIST[n])+ "cm。\n"
                        replySTR = answerSTR
                        
                        
                    elif mscDICT[client.user.id]["request"] =="height.min":  #最矮
                        indexLIST=minIndex(heightLIST)
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR+=ProfileDICT[mscDICT[client.user.id]["group"]][n]["JName"]+"，他 "+str(heightLIST[n])+ "cm。\n"
                        replySTR =answerSTR
                        
    
                    elif mscDICT[client.user.id]["request"] =="height.sort.LtoH":  #矮到高
                        sortedLIST=sorted(heightLIST)
                        indexLIST=[]
                        for n in range(len(heightLIST)):
                            indexLIST.append(heightLIST.index(sortedLIST[n]))
                        lostIndex=[]
                        for n in range(min(indexLIST),max(indexLIST)):
                            if n not in indexLIST:
                                lostIndex.append(n)
                        for e in indexLIST:
                            if indexLIST.count(e)>1:
                                for l in lostIndex:
                                  indexLIST[indexLIST.index(e)]= l
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']+"，"+str(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])+"cm\n"
                            replySTR = "身高從矮到高是：\n"+answerSTR
                        
                        
                    elif mscDICT[client.user.id]["request"] =="height.sort.HtoL":  #高到矮
                        sortedLIST=sorted(heightLIST)
                        sortedLIST.reverse()
                        indexLIST=[]
                        for n in range(len(heightLIST)):
                            indexLIST.append(heightLIST.index(sortedLIST[n]))
                        lostIndex=[]
                        for n in range(min(indexLIST),max(indexLIST)):
                            if n not in indexLIST:
                                lostIndex.append(n)
                        for e in indexLIST:
                            if indexLIST.count(e)>1:
                                for l in lostIndex:
                                  indexLIST[indexLIST.index(e)]= l
                        answerSTR=""
                        for n in indexLIST:
                            answerSTR += ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']+"，"+str(ProfileDICT[mscDICT[client.user.id]["group"]][n]['height'])+"cm\n"
                            replySTR = "身高從高到矮是：\n"+answerSTR
                        
                       
                elif mscDICT[client.user.id]["request"].encode('UTF-8').isalnum() == True: #request是身高
                    replySTR= mscDICT[client.user.id]["member"]+"，他 "+str(findHeight(mscDICT[client.user.id]["member"]))+" cm。"
                    
                
                elif mscDICT[client.user.id]["request"].encode('UTF-8').isalpha() == False: 
    
                    if len(mscDICT[client.user.id]["request"]) == 2 :
                        if mscDICT[client.user.id]["request"].isdigit() == True: #距離生日的天數是兩位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                        
                        else:
                            memberLIST=findBlood(mscDICT[client.user.id]["group"],mscDICT[client.user.id]["request"])
                            if memberLIST == 'no': #沒有是該血型的人
                                replySTR=mscDICT[client.user.id]["group"]+" 中沒有寫血型是 "+mscDICT[client.user.id]["request"]+" 的成員。"
                            
                            elif type(memberLIST)==list:
                                answerSTR=""
                                for n in range(len(memberLIST)):
                                    answerSTR+=memberLIST[n]+" "
                                replySTR =answerSTR+"是 "+mscDICT[client.user.id]["request"]+"。"
                           
                            else: #回報血型
                                replySTR="他是 "+mscDICT[client.user.id]["request"]+" 。"
                            
                    
                    elif 2< len(mscDICT[client.user.id]["request"]) <5 : #request是地名
                        if mscDICT[client.user.id]["member"] == 'no': #沒有來自該地的人
                            replySTR=mscDICT[client.user.id]["group"]+" 中沒有來自 "+mscDICT[client.user.id]["request"]+" 的成員。"
                            
                        elif mscDICT[client.user.id]["request"].isdigit() == True: #距離生日的天數是三位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                            
                        else: #回報地名
                            replySTR="他來自 "+mscDICT[client.user.id]["request"]+" 。"
                            
                            
                    else: #request是生日
                        if mscDICT[client.user.id]["request"].isdigit(): #距離生日的天數是個位數
                            replySTR="離 "+mscDICT[client.user.id]["member"]+" 的生日還有 "+mscDICT[client.user.id]["request"]+" 天。"
                            
                        else: #request是生日
                            replySTR="他的生日是 "+mscDICT[client.user.id]["request"]+" 。"
                            
                    
            elif type(mscDICT[client.user.id]["request"]) == list:  #回報多個問題
                for e in mscDICT[client.user.id]["request"]:
                    if e in ("age.max","age.min"):
                        ageLIST=[]
                        for n in range(len(ProfileDICT[mscDICT[client.user.id]["group"]])) :
                            ageLIST.append(findAge(ProfileDICT[mscDICT[client.user.id]["group"]][n]['JName']))
                        if e == 'age.max': #回報最年長
                            maxLIST=[]
                            indexLIST=maxIndex(ageLIST)
                            if len(indexLIST) != 1:  #如果很多人同歲比較生日
                                birthLIST=[]
                                for i in indexLIST:
                                    birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                                index=birthLIST.index(min(birthLIST))
                                maxLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName'])
                                maxLIST.append(ageLIST[indexLIST[index]])
                            else: #len(indexLIST) == 1
                                index=ageLIST.index(max(ageLIST))
                                maxLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName'])
                                maxLIST.append(str(ageLIST[index]))
                        if e == 'age.max': #回報最年長
                            minLIST=[]
                            indexLIST=minIndex(ageLIST)
                            if len(indexLIST) != 1:  #如果很多人同歲比較生日
                                birthLIST=[]
                                for i in indexLIST:
                                    birthLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][i]['Birth'])
                                index=birthLIST.index(max(birthLIST))
                                minLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][indexLIST[index]]['JName'])
                                minLIST.append(ageLIST[indexLIST[index]])
                            else: #len(indexLIST) == 1
                                index=ageLIST.index(min(ageLIST))
                                minLIST.append(ProfileDICT[mscDICT[client.user.id]["group"]][index]['JName'])
                                minLIST.append(str(ageLIST[index]))
                        print(maxLIST)
                        print(minLIST)
                        replySTR=f'最年長是 {maxLIST[0]}，{maxLIST[1]} 歲。\n最年幼是 {minLIST[0]}，{minLIST[1]} 歲。'
                        
       
        if msgSTR in ("謝謝","我問完了","掰掰","88","bye","byebye","再見","再會"):
            replySTR = "感謝你的使用，期待再次相見~"
            mscDICT[client.user.id]["completed"]=True

        if mscDICT[client.user.id]["completed"]:    # 清空 User Dict
            del mscDICT[client.user.id]
        
        print(replySTR)
        
        if replySTR:    # 回應 User 訊息
            await message.reply(replySTR)
        return




if __name__ == "__main__":
    client.run(DISCORD_TOKEN)

    #getLokiResult("")
