#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
import os
import re

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

CWD_PATH = os.path.dirname(os.path.abspath(__file__))
MODULE_DICT = {
    "Account": import_from_path("Money_add_Account", os.path.join(CWD_PATH, "lib/Account.py")),
    "LLM": import_from_path("Money_add_lib_LLM", os.path.join(CWD_PATH, "lib/LLM.py")),
    "Project": import_from_path("Money_add_lib_Project", os.path.join(CWD_PATH, "lib/Project.py")),
}
"""
Account 變數清單
[變數] BASE_PATH         => 根目錄位置
[變數] LIB_PATH          => lib 目錄位置
[變數] INTENT_PATH       => intent 目錄位置
[變數] REPLY_PATH        => reply 目錄位置
[變數] ACCOUNT_DICT      => account.info 內容
[變數] ARTICUT           => ArticutAPI (用法：ARTICUT.parse()。 #需安裝 ArticutAPI.)
[變數] USER_DEFINED_FILE => 使用者自定詞典的檔案路徑
[變數] USER_DEFINED_DICT => 使用者自定詞典內容
"""
ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
ARTICUT = MODULE_DICT["Account"].ARTICUT
USER_DEFINED_FILE = MODULE_DICT["Account"].USER_DEFINED_FILE
getCosineSimilarity = MODULE_DICT["LLM"].getCosineSimilarity
getLLM = MODULE_DICT["LLM"].getLLM
COMM_TEST = MODULE_DICT["Project"].COMM_TEST
cosSimilarLoki = MODULE_DICT["Project"].cosSimilarLoki
execLoki = MODULE_DICT["Project"].execLoki


#============== Function ==============
def getSimilarity(input1STR, input2STR, featureLIST=ACCOUNT_DICT["utterance_feature"], userDefinedDictFILE=USER_DEFINED_FILE):
    """
    input
        input1STR              STR      文本1
        input2STR              STR      文本2
        featureLIST            STR[]    比對的 feature (noun, verb, contentword)
        userDefinedDictFILE    STR      使用者自定詞典的檔案路徑

    output
        score                  FLOAT    本文 1 和 2 兩者的餘弦相似度
    """
    score = getCosineSimilarity(input1STR, input2STR, featureLIST, userDefinedDictFILE)
    return score

def askLoki(content, **kwargs):
    """
    input
        content       STR / STR[]    要執行 Loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        refDICT       DICT           參考內容
        toolkitDICT   DICT           工具箱

    output
        resultDICT    DICT           合併 runLoki() 的結果

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    filterLIST = kwargs["filterLIST"] if "filterLIST" in kwargs else []
    splitLIST = kwargs["splitLIST"] if "splitLIST" in kwargs else []
    refDICT = kwargs["refDICT"] if "refDICT" in kwargs else {}
    toolkitDICT = kwargs["toolkitDICT"] if "toolkitDICT" in kwargs else {}

    resultDICT = execLoki(content, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT, toolkitDICT=toolkitDICT)
    return resultDICT

def askLLM(system="", assistant="", user=""):
    """
    input
        system       STR    設定 system role 的 content
        assistant    STR    設定 assistant role 的 content
        user         STR    設定 user role 的 content

    output
        response     STR    LLM 返回結果
    """
    return getLLM(system, assistant, user)

def simLoki(content, **kwargs):
    """
    input
        content       STR / STR[]    要執行 Loki Similarity 的內容 (可以是字串或字串列表)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                           * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content
        featureLIST   STR[]          CosineSimilarity 計算時使用的參數

    output
        resultDICT    DICT           相似度結果 {intent: input }
    """
    splitLIST = kwargs["splitLIST"] if "splitLIST" in kwargs else ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    featureLIST = kwargs["featureLIST"] if "featureLIST" in kwargs else []

    resultDICT = cosSimilarLoki(content, splitLIST=splitLIST, featureLIST=featureLIST)
    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    contentSTR = ""
    if not contentSTR and "utterance_count" in ACCOUNT_DICT and ACCOUNT_DICT["utterance_count"]:
        intentSTR = list(ACCOUNT_DICT["utterance_count"])[0]
        contentSTR = list(ACCOUNT_DICT["utterance_count"][intentSTR])[0]
        contentSTR = re.sub("[\[\]]", "", contentSTR)

    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    # 設定參考資料
    refDICT = { # value 必須為 list
        #"key": []
    }

    # 檢測功能是否正常
    COMM_TEST(contentSTR)

    # 執行 Loki
    resultDICT = askLoki(contentSTR, filter=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    pprint(resultDICT)
