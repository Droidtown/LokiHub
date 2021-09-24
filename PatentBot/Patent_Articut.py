#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from collections import Counter
from ArticutAPI import Articut
import json
import math
#import Dataset.patent as patent

def wordExtractor(inputLIST, unify=True):
    '''
    配合 Articut() 的 .getNounStemLIST() 和 .getVerbStemLIST() …等功能，拋棄位置資訊，只抽出詞彙。
    '''
    resultLIST = []
    for i in inputLIST:
        if i == []:
            pass
        else:
            for e in i:
                resultLIST.append(e[-1])
    if unify == True:
        return sorted(list(set(resultLIST)))
    else:
        return sorted(resultLIST)


def counterCosineSimilarity(counter01, counter02, w=1):  # 這裡可以改權重做分析
    '''
    計算 counter01 和 counter02 兩者的餘弦相似度
    '''
    terms = set(counter01).union(counter02)
    dotprod = sum(counter01.get(k, 0) * counter02.get(k, 0) for k in terms)
    magA = math.sqrt(sum(counter01.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(counter02.get(k, 0)**2 for k in terms))
    return (dotprod / (magA * magB))*w



def articut4PatentBot(categoryFILE, inputSTR):
    with open("account.info", encoding="utf-8") as f:
        userinfoDICT = json.loads(f.read())

    articut = Articut(username=userinfoDICT["username"], apikey=userinfoDICT["apikey"], level="lv1")

    # 讀入對應類別的專利文本
    #patentDICT = patent[categoryFILE]
    #patent_file = categoryFILE + '.json'
    with open("Dataset\patent.json", encoding='utf-8') as f:
        AllpatentDICT = json.loads(f.read())
        patentDICT = AllpatentDICT[categoryFILE]

    CertificateNumber = list(patentDICT.keys())

    # 接收使用者輸入的專利範圍
    userSTR = inputSTR.replace(" ", "").replace("\n", "")
    userResultDICT = articut.parse(userSTR)

    # 將類別中的專利範圍全部比對一次
    VerbCosineSimilarity = []
    NounCosineSimilarity = []
    TFIDFCosineSimilarity = []
    for k in patentDICT.values():
        STR = k.replace(" ", "").replace("\n", "")
        STRResultDICT = articut.parse(STR)
    
        # 取得「動詞」做為特徵列表
        patentVerbLIST = articut.getVerbStemLIST(STRResultDICT)
        userVerbLIST = articut.getVerbStemLIST(userResultDICT)
        # 利用 Counter() 模組計算每個動詞出現的次數
        patentCOUNT = Counter(wordExtractor(patentVerbLIST, unify=True))
        userCOUNT = Counter(wordExtractor(userVerbLIST, unify=True))
        # 計算 [專利文本 vs. 使用者輸入文本] 的餘弦相似度
        patent2userSIM = counterCosineSimilarity(patentCOUNT, userCOUNT)
        VerbCosineSimilarity.append(patent2userSIM)
    
    
    
        # 取得「名詞」做為特徵列表
        patentNounLIST = articut.getNounStemLIST(STRResultDICT)
        userNounLIST = articut.getNounStemLIST(userResultDICT)
        # 利用 Counter() 模組計算每個名詞出現的次數
        patentCOUNT = Counter(wordExtractor(patentNounLIST, unify=True))
        userCOUNT = Counter(wordExtractor(userNounLIST, unify=True))
        # 計算 [專利文本 vs. 使用者輸入文本] 的餘弦相似度
        patent2userSIM = counterCosineSimilarity(patentCOUNT, userCOUNT)
        NounCosineSimilarity.append(patent2userSIM)
    
    
    
        # 取得「TF-IDF」做為特徵列表
        patentTFIDFLIST = articut.analyse.extract_tags(STRResultDICT)
        userTFIDFLIST = articut.analyse.extract_tags(userResultDICT)
        # 利用 Counter() 模組計算每個 TF-IDF 特徵詞出現的次數
        patentCOUNT = Counter(patentTFIDFLIST)
        userCOUNT = Counter(userTFIDFLIST)
        # 計算 [專利文本 vs. 使用者輸入文本] 的 TF-IDF 餘弦相似度
        patent2userSIM = counterCosineSimilarity(patentCOUNT, userCOUNT)
        TFIDFCosineSimilarity.append(patent2userSIM)


    ArticutresultDICT = {}
    max_Verb = max(VerbCosineSimilarity)
    v = VerbCosineSimilarity.index(max_Verb)
    # print("[專利文本 vs. 使用者輸入文本] 的動詞餘弦相似度:{}".format(VerbCosineSimilarity))
    # print("最大值為{:.2f}來自證書書號{}的專利範圍".format(max_Verb, CertificateNumber[v]))
    ArticutresultDICT["Verb"] = {}
    ArticutresultDICT["Verb"][CertificateNumber[v]] = max_Verb

    max_Noun = max(NounCosineSimilarity)
    n = NounCosineSimilarity.index(max_Noun)
    # print("[專利文本 vs. 使用者輸入文本] 的名詞餘弦相似度:{}".format(NounCosineSimilarity))
    # print("最大值為{:.2f}來自證書書號{}的專利範圍".format(max_Noun, CertificateNumber[n]))
    ArticutresultDICT["Noun"] = {}
    ArticutresultDICT["Noun"][CertificateNumber[n]] = max_Noun

    max_TFIDF = max(TFIDFCosineSimilarity)
    t = TFIDFCosineSimilarity.index(max_TFIDF)
    # print("[專利文本 vs. 使用者輸入文本] 的 TF-IDF 特徵詞餘弦相似度:{}".format(TFIDFCosineSimilarity))
    # print("最大值為{:.2f}來自證書書號{}的專利範圍".format(max_TFIDF, CertificateNumber[t]))
    ArticutresultDICT["TFIDF"] = {}
    ArticutresultDICT["TFIDF"][CertificateNumber[t]] = max_TFIDF

    ArticutresultDICT["All_Max"] = {}
    m = max(max_Verb, max_Noun, max_TFIDF)
    if m == max_Noun:
        ArticutresultDICT["All_Max"][CertificateNumber[n]] = [m, "名詞"]
    elif m == max_Verb:
        ArticutresultDICT["All_Max"][CertificateNumber[v]] = [m, "動詞"]
    elif m == max_TFIDF:
        ArticutresultDICT["All_Max"][CertificateNumber[t]] = [m, "TF-IDF"]


    return ArticutresultDICT


# 測試用
# inputSTR = '1.一種便當預購系統，包含：一多媒體機，設置於一實體門市內，該多媒體機接收一訂購資料，並經由一網路傳送該訂購資料，於接收一完成訂購通知後，列印一繳費單，其中該繳費單包括一訂單代碼；一收銀機，設置於該實體門市，該收銀機接收該繳費單之該訂單代碼，傳送該訂單代碼並接收對應之該訂購資料，接收並傳送一付款確認通知，且依據該訂單代碼及該訂購資料列印一取貨單；以及一預購伺服器，經由該網路接收該訂購資料，並響應該訂購資料以產生及傳送對應的該完成訂購通知至該多媒體機，且經由該網路接收來自該收銀機的該訂單代碼，並響應該訂單代碼以檢索並傳送對應的該訂購資料至該收銀機，以及經由該網路接收來自該收銀機的該付款確認通知，並響應該付款確認通知發送對應的一訂購通知。2.如請求項 1 所述之便當預購系統，其中該訂購資料更包括該實體門市之一門市資料。3.如請求項 1 所述之便當預購系統，更包含一廠商伺服器，通訊連接該預購伺服器，該訂購資料包括一取貨日期，該預購伺服器依據該取貨日期，於該取貨日期前之一預定時間傳送該訂購資料至該廠商伺服器。4.如請求項 3 所述之便當預購系統，其中，該收銀機於讀取該取貨單上之該訂單代碼後，確認自讀取時的時間至該訂單資料之該取貨日期是否大於該預定時間，若是則該收銀機於接收一確認退貨通知後，傳送至該預購伺服器。5.如請求項 1 所述之便當預購系統，其中該訂購資料包含一個人資訊，該預購伺服器於接收該付款確認通知後，響應該付款確認通知，依據該個人資訊發送該訂單代碼及該訂購資料。6.一種便當預購系統，包含：一行動裝置，接收一訂購資料，並經由一網路傳送該訂購資料，於接收一完成訂購通知後，顯示一繳費條碼，其中該繳費條碼包括一訂單代碼；一收銀機，設置於一實體門市，該收銀機接收該繳費條碼以取得該訂單代碼，傳送該訂單代碼並接收對應之該訂購資料，接收並傳送一付款確認通知，且依據該訂單代碼及該訂購資料列印一取貨單；以及一預購伺服器，經由該網路接收該訂購資料，並響應該訂購資料以產生及傳送對應的該完成訂購通知至該行動裝置，且經由該網路接收來自該收銀機的該訂單代碼，並響應該訂單代碼以檢索並傳送對應的該訂購資料至該收銀機，以及經由該網路接收來自該收銀機的該付款確認通知，並響應該付款確認通知發送對應的一訂購通知。7.如請求項 6 所述之便當預購系統，其中該訂購資料更包括該實體門市之一門市資料。8.如請求項 6 所述之便當預購系統，更包含一廠商伺服器，通訊連接該預購伺服器，該訂購資料包括一取貨日期，該預購伺服器依據該取貨日期，於該取貨日期前之一預定時間傳送該訂購資料至該廠商伺服器。9.如請求項 8 所述之便當預購系統，其中，該收銀機於讀取該取貨單上之該訂單代碼後，確認自讀取時的時間至該訂單資料之該取貨日期是否大於該預定時間，若是則該收銀機於接收一確認退貨通知後，傳送至該預購伺服器。10.   如請求項 6 所述之便當預購系統，其中該訂購資料包含一個人資訊，該預購伺服器於接收該付款確認通知後，響應該付款確認通知，依據該個人資訊發送該訂單代碼及該訂購資料。'
# category = 'G06Q_020_28_M'
# print(articut4PatentBot(category, inputSTR))
