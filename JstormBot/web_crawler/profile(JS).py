# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:46:36 2021

@author: Hao
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 19:33:41 2021

@author: HAO
"""

import requests
from bs4 import BeautifulSoup

soup=[]
for n in range(3,8):
    url = 'https://www.j-storm.co.jp/s/js/artist/J000'+str(n)+'/profile?ima=0000'
    response = requests.get(url)
    soup.append(BeautifulSoup(response.text, "html.parser"))
    #print(soup.prettify())  #輸出排版後的HTML內容

l1=[]
l2=[]
Group=['TOKIO','嵐','KAT-TUN','Hey! Say! JUMP']
for n in range(0,len(soup)):
    result=soup[n].find_all('article')
    img=soup[n].find_all("img","sp-none")

    for r in result:
        l1.append(r.text)

    for i in img:
        l2.append(i['src'])
        
        
JSurl= 'https://www.j-storm.co.jp/s/js/?ima=0000'
JSresponse = requests.get(JSurl)
JSsoup=BeautifulSoup(JSresponse.text, "html.parser")
groupLIST=['color-tokio','color-arashi first','color-kattun','color-heysayjump']
l3=[]

for n in range(0,len(groupLIST)):
    Gresult=JSsoup.find('figure',groupLIST[n])
    Presult=Gresult.find('img')
    l3.append(Presult['src'])

ProfileLIST=[]
for n in range(0,len(l1)):
    if len(l1[n].split()[0])<4:
        J_first_name=l1[n].split()[1]
        J_last_name=l1[n].split()[0]
        E_first_name=l1[n].split()[2]
        E_last_name=l1[n].split()[3]
        Birth=l1[n].split()[4]
        Birth=Birth.replace("生まれ","")
        Born=l1[n].split()[5]
        Born=Born.replace("出身","")
        Blood=l1[n].split()[6]
    
    else:
        J_first_name=l1[n].split()[0][2:]
        J_last_name=l1[n].split()[0][:2]
        E_first_name=l1[n].split()[1]
        E_last_name=l1[n].split()[2]
        Birth=l1[n].split()[3]
        Birth=Birth.replace("生まれ","")
        Born=l1[n].split()[4]
        Born=Born.replace("出身","")
        Blood=l1[n].split()[5]
    
    
    dic={"JName":J_last_name+J_first_name,
         "JFname":J_first_name,
         "JLname":J_last_name,
         "EName":E_first_name+" "+E_last_name,
         "EFname":E_first_name,
         "ELname":E_last_name,
         "Birth":Birth ,
         "Born":Born ,
         "Blood":Blood,
         "Pic":'https://www.j-storm.co.jp'+l2[n]}
    
            
    ProfileLIST.append(dic)

colorLIST=['藍','綠','紫','綠','紫','黃','藍','紅','粉','藍','紫','紅','粉','天藍','橘','紫','藍','黃','黃綠']
heightLIST=[167,170,182,176,174,168,166,173,172,170,176,164,158,180,164,176,173,175,179]

for n in range(0,len(colorLIST)):
    ProfileLIST[n]['color']=colorLIST[n]
    ProfileLIST[n]['height']=heightLIST[n]
    
ProfileDICT={Group[0]:ProfileLIST[:3],Group[1]:ProfileLIST[3:8],Group[2]:ProfileLIST[8:11],Group[3]:ProfileLIST[11:]}

GroupDICT={}
GroupDICT['TOKIO']={'formationdate':'1994.4','debutdate':'1994.9.21','Pic':'https://www.j-storm.co.jp'+l3[0]}
GroupDICT['嵐']={'formationdate':'1999.9.15','debutdate':'1999.11.3','Pic':'https://www.j-storm.co.jp'+l3[1]}
GroupDICT['KAT-TUN']={'formationdate':'2001.3.6','debutdate':'2006.3.22','Pic':'https://www.j-storm.co.jp'+l3[2]}
GroupDICT['Hey! Say! JUMP']={'formationdate':'2007.9.24','debutdate':'2007.11.14','Pic':'https://www.j-storm.co.jp'+l3[3]}


import json
with open('ProfileDICT.json', 'w') as f:
      json.dump(ProfileDICT,f)
    
with open('GroupDICT.json', 'w') as f:
      json.dump(GroupDICT,f)
    


    