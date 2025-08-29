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
    "Account": import_from_path("RSBot_lib_Account", os.path.join(CWD_PATH, "lib/Account.py")),
    "LLM": import_from_path("RSBot_lib_LLM", os.path.join(CWD_PATH, "lib/LLM.py")),
    "Project": import_from_path("RSBot_lib_Project", os.path.join(CWD_PATH, "lib/Project.py")),
}
"""
Account Variables
[Variable] BASE_PATH         => path of root
[Variable] LIB_PATH          => path of lib folder
[Variable] INTENT_PATH       => path of intent folder
[Variable] REPLY_PATH        => path of reply folder
[Variable] ACCOUNT_DICT      => account.info
[Variable] ARTICUT           => ArticutAPI (Usage: ARTICUT.parse()。 #ArticutAPI Required.)
[Variable] USER_DEFINED_FILE => path of UserDefined
[Variable] USER_DEFINED_DICT => UserDefined data
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
        input1STR              STR      sentence1
        input2STR              STR      sentence2
        featureLIST            STR[]    compare features (noun, verb, contentword)
        userDefinedDictFILE    STR      path of UserDefined.json

    output
        score                  FLOAT    The cosine similarity between sentence1 and sentence2.
    """
    score = getCosineSimilarity(input1STR, input2STR, featureLIST, userDefinedDictFILE)
    return score

def askLoki(content, **kwargs):
    """
    input
        content       STR / STR[]    analyze by loki (string or string list)
        filterLIST    STR[]          specific intents (empty: all intent)
        splitLIST     STR[]          split by symbols (empty: don't split)
                                     * using splitLIST if the content includes multiple utterances with an intent
        refDICT       DICT           references
        toolkitDICT   DICT           toolbox

    output
        resultDICT    DICT           results of runLoki()

    e.g.
        splitLIST = ["!", ",", ".", "\\n", "\\u3000", ";"]
        resultDICT = execLoki("How is the weather today? How is the weather tomorrow?")                      # output => ["weather today"]
        resultDICT = execLoki("How is the weather today? How is the weather tomorrow?", splitLIST=splitLIST) # output => ["weather today", "weather tomorrow"]
        resultDICT = execLoki(["How is the weather today?", "How is the weather tomorrow?"])                 # output => ["weather today", "weather tomorrow"]
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
        system       STR    set system role content
        assistant    STR    set assistant role content
        user         STR    set user role content

    output
        response     STR    LLM's response
    """
    return getLLM(system, assistant, user)

def simLoki(content, **kwargs):
    """
    input
        content       STR / STR[]    similarity with loki (string or string list)
        splitLIST     STR[]          split by symbols (empty: don't split)
                                     * using splitLIST if the content includes multiple utterances with an intent
        featureLIST   STR[]          feature of cosine similarity

    output
        resultDICT    DICT           similarity {intent: input }
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
    # set references
    refDICT = { # value is a list
        #"key": []
    }

    # Testing the function
    COMM_TEST(contentSTR)

    # Run Loki
    resultDICT = askLoki(contentSTR, filter=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    pprint(resultDICT)
