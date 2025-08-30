#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ingredient

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""

from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
import json
import os

INTENT_NAME = "ingredient"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULE_DICT = {
    "Account": import_from_path("whats_in_my_fridge_lib_Account", os.path.join(os.path.dirname(CWD_PATH), "lib/Account.py")),
}

ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
USER_DEFINED_DICT = MODULE_DICT["Account"].USER_DEFINED_DICT

def debugInfo(inputSTR, utterance):
    if ACCOUNT_DICT["debug"]:
        print("[{}] {} ===> {}".format(INTENT_NAME, inputSTR, utterance))

def extract_ingredients_by_utterance(utterance, args):
    """掃描所有 args，返回所有參數讓 validate_ingredients 來篩選"""
    return args

def validate_ingredients(ingredients):
    """驗證食材是否在 USER_DEFINED_DICT 中"""
    # 取得所有食材類別
    all_ingredients = []
    ingredient_categories = ["_veg_", "_fruit_", "_meat_", "_seafood_", "_grain_", "_otherfood_"]
    
    for category in ingredient_categories:
        if category in USER_DEFINED_DICT:
            all_ingredients.extend(USER_DEFINED_DICT[category])
    
    valid_ingredients = []
    for ingredient in ingredients:
        if ingredient in all_ingredients:
            valid_ingredients.append(ingredient)
    
    return valid_ingredients

def merge_and_dedupe(existing_ingredients, new_ingredients):
    """合併並去重，保持順序"""
    all_ingredients = existing_ingredients + new_ingredients
    seen = set()
    result = []
    
    for ingredient in all_ingredients:
        if ingredient not in seen:
            seen.add(ingredient)
            result.append(ingredient)
    
    return result

def format_ingredients_chinese(ingredients):
    """繁體中文友善的食材連接"""
    if len(ingredients) == 1:
        return ingredients[0]
    elif len(ingredients) == 2:
        return f"{ingredients[0]}和{ingredients[1]}"
    else:
        return "、".join(ingredients[:-1]) + f"和{ingredients[-1]}"

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    debugInfo(inputSTR, utterance)
    
    # 初始化
    if "ingredients" not in resultDICT:
        resultDICT["ingredients"] = []
    
    # 提取食材
    extracted_ingredients = extract_ingredients_by_utterance(utterance, args)
    
    # 驗證食材
    valid_ingredients = validate_ingredients(extracted_ingredients)
    
    if valid_ingredients:
        # 合併並去重
        resultDICT["ingredients"] = merge_and_dedupe(resultDICT["ingredients"], valid_ingredients)
        
        # 格式化回覆
        ingredients_str = format_ingredients_chinese(resultDICT["ingredients"])
        resultDICT["response"] = f"好的，現在我們有{ingredients_str}，請問要做幾人份的料理呢？"
        resultDICT["intent"] = "ingredient_input"
    else:
        resultDICT["intent"] = "unknown"
        resultDICT["response"] = "不好意思，我不太理解你的意思，可以重複一遍嗎？"
    
    return resultDICT


if __name__ == "__main__":
    from pprint import pprint

    # 測試
    test_cases = [
        ("[蔥]", ["蔥"]),
        ("[青椒]和[魚]", ["青椒", "魚"]),
        ("[今天]買了[番茄]跟[雞蛋]", ["今天", "番茄", "雞蛋"]),
        ("[我]買了[未知食材]", ["我", "未知食材"]),  # 測試失敗情況
    ]
    
    for utterance, args in test_cases:
        print(f"\n測試: {utterance}")
        print(f"參數: {args}")
        result = getResult("test", utterance, args, {}, {})
        pprint(result)