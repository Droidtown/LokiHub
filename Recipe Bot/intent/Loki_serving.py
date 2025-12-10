#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for serving

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
import re

INTENT_NAME = "serving"
CWD_PATH = os.path.dirname(os.path.abspath(__file__))

def import_from_path(module_name, file_path):
    spec = spec_from_file_location(module_name, file_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULE_DICT = {
    "Account": import_from_path("whats_in_my_fridge_lib_Account", os.path.join(os.path.dirname(CWD_PATH), "lib/Account.py")),
    "LLM": import_from_path("whats_in_my_fridge_lib_LLM", os.path.join(os.path.dirname(CWD_PATH), "lib/LLM.py"))
}

ACCOUNT_DICT = MODULE_DICT["Account"].ACCOUNT_DICT
USER_DEFINED_DICT = MODULE_DICT["Account"].USER_DEFINED_DICT

def debugInfo(inputSTR, utterance):
    if ACCOUNT_DICT["debug"]:
        print("[{}] {} ===> {}".format(INTENT_NAME, inputSTR, utterance))

def _extract_number_zh(text: str) -> int:
    """提取中文和阿拉伯數字，轉換為數字"""
    zh_num_map = {
        "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
        "兩": 2, "零": 0
    }
    
    text = re.sub(r"\s+", "", text)
    
    # 阿拉伯數字
    arabic_match = re.search(r"\d+", text)
    if arabic_match:
        return int(arabic_match.group())
    
    # 中文數字
    if text in zh_num_map:
        return zh_num_map[text]
    
    # 複合中文數字（十一、十二等）
    if "十" in text:
        if text == "十":
            return 10
        elif text.startswith("十"):  # 十一, 十二, ...
            unit = text[1:]
            if unit in zh_num_map:
                return 10 + zh_num_map[unit]
        elif text.endswith("十"):  # 二十, 三十, ...
            tens = text[:-1]
            if tens in zh_num_map:
                return zh_num_map[tens] * 10
        else:  # 二十一, 三十二, ...
            parts = text.split("十")
            if len(parts) == 2 and parts[0] in zh_num_map:
                tens = zh_num_map[parts[0]] * 10
                units = zh_num_map.get(parts[1], 0) if parts[1] else 0
                return tens + units
    
    return None

def _extract_serving_count(args_list, input_text):
    """
    提取份數，實作優先級邏輯
    返回: (count, intent_type)
    """
    # 獲取 serving unit 列表
    serving_units = USER_DEFINED_DICT.get("_servingunit_", ["人", "人份", "份", "口"])
    
    # 優先級1: 數字 + serving unit
    # 先檢查 input_text 本身是否包含完整的 "數字+單位" 組合
    for unit in serving_units:
        number_pattern = r"([一二三四五六七八九十兩零]{1,3}|\d+)" + unit
        matches = re.finditer(number_pattern, input_text)
        
        for match in matches:
            number_text = match.group(1)
            extracted_number = _extract_number_zh(number_text)
            if extracted_number and 1 <= extracted_number <= 20:
                return extracted_number, "serving_input"
    
    # 再檢查 args 中分離的數字+單位組合
    for i, arg in enumerate(args_list):
        extracted_number = _extract_number_zh(arg)
        if extracted_number and 1 <= extracted_number <= 20:
            # 檢查後面的 args 或 input_text 是否包含 serving unit
            remaining_args = args_list[i + 1:] + [input_text]
            for next_arg in remaining_args:
                if any(unit in next_arg for unit in serving_units):
                    return extracted_number, "serving_input"
    
    # 優先級2: 情侶類關鍵字
    combined_text = "".join(args_list) + input_text
    couple_keywords = ["夫妻", "情侶", "燭光"]
    for keyword in couple_keywords:
        if keyword in combined_text:
            return 2, "serving_input"
    
    # 優先級3: 模糊類關鍵字
    vague_keywords = ["家庭", "聚餐", "派對", "多人", "少人", "大份", "小份"]
    
    # 檢查模糊關鍵字
    for keyword in vague_keywords:
        if keyword in combined_text:
            return None, "serving_clarification"
    
    # 檢查單獨的 serving unit（沒有前面的數字）
    for unit in serving_units:
        if unit in combined_text:
            # 確認這個單位前面沒有緊跟著數字
            unit_with_number_pattern = r"[一二三四五六七八九十兩零\d]+" + unit
            if not re.search(unit_with_number_pattern, combined_text):
                return None, "serving_clarification"
    
    # 優先級4: 其他情況
    return None, "unknown"

def _has_serving_relevance(args_list, input_text):
    """
    檢查輸入是否與份數相關
    用於判斷是 serving_clarification 還是 unknown
    """
    combined_text = "".join(args_list) + input_text
    
    # 份數相關的關鍵字
    serving_related = [
        "人", "份", "口", "個人", "家庭", "聚餐", "派對", 
        "多人", "少人", "大份", "小份", "夫妻", "情侶", "燭光",
        "人份", "客人", "朋友", "家人"
    ]
    
    return any(keyword in combined_text for keyword in serving_related)

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    """
    serving intent 主要處理函數
    """
    debugInfo(inputSTR, utterance)
    
    # 提取份數信息
    serving_count, intent_type = _extract_serving_count(args, inputSTR)
    
    if intent_type == "serving_input":
        # 成功提取到數字
        resultDICT["intent"] = "serving_input"
        resultDICT["servings"] = {"count": serving_count}
        
    elif intent_type == "serving_clarification":
        # 需要詢問具體人數
        resultDICT["intent"] = "serving_clarification"
        
    else:  # intent_type == "unknown"
        # 檢查是否與份數相關
        if _has_serving_relevance(args, inputSTR):
            resultDICT["intent"] = "serving_clarification"
        else:
            resultDICT["intent"] = "unknown"
    
    return resultDICT


if __name__ == "__main__":
    """測試"""
    from pprint import pprint
    
    test_cases = [
        # 優先級1: 數字+單位
        ("一人份", "[一]人份", ["一"]),
        ("三個人", "[三個]人", ["三", "個"]),
        ("五人份料理", "[五]人份[料理]", ["五", "料理"]),
        ("四口人", "[四]口人", ["四", "口", "人"]),
        
        # 優先級2: 情侶類
        ("夫妻晚餐", "[夫妻]晚餐", ["夫妻"]),
        ("情侶聚餐", "[情侶]聚餐", ["情侶"]),
        ("燭光晚餐", "[燭光]晚餐", ["燭光"]),
        
        # 優先級3: 模糊類
        ("家庭聚餐", "[家庭]聚餐", ["家庭"]),
        ("大份的", "[大份]的", ["大份"]),
        ("多人份", "多人份", ["多人份"]),
        ("人份", "人份", ["人份"]),  # 單獨serving unit
        
        # 優先級4: 無關
        ("今天天氣真好", "今天天氣真好", ["今天", "天氣", "真好"]),
        ("我餓了", "我餓了", ["我", "餓", "了"]),
        
        # 邊界情況
        ("零人份", "[零]人份", ["零"]),  # 無效數字
        ("一百人份", "[一百]人份", ["一百"]),  # 超出範圍
        ("三四個人", "[三四個]人", ["三四個"]),  # 複雜數字
        ("小份兩人", "[小份][兩]人", ["小份", "兩"]),  # 優先級衝突
    ]
    
    print("=== Serving Intent 測試 ===")
    for inputSTR, utterance, args in test_cases:
        resultDICT = {}
        result = getResult(inputSTR, utterance, args, resultDICT, {})
        
        print(f"\n輸入: {inputSTR}")
        print(f"結果: {result}")
        
        # 簡化顯示
        if result.get("intent") == "serving_input":
            count = result.get("servings", {}).get("count", "?")
            print(f"  → 提取到: {count}人份")
        elif result.get("intent") == "serving_clarification":
            print(f"  → 需要詢問具體人數")
        elif result.get("intent") == "unknown":
            print(f"  → 無關輸入")