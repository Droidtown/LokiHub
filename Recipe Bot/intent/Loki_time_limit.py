#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for time_limit

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

INTENT_NAME = "time_limit"
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

def _extract_number_zh(text: str) -> float:
    """提取中文和阿拉伯數字，轉換為數字（支援小數）"""
    zh_num_map = {
        "一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
        "六": 6, "七": 7, "八": 8, "九": 9, "十": 10,
        "兩": 2, "零": 0, "半": 0.5
    }
    
    text = re.sub(r"\s+", "", text)
    
    # 處理特殊情況：一個半、兩個半等
    compound_pattern = r"([一二三四五]?)個?半"
    compound_match = re.search(compound_pattern, text)
    if compound_match:
        base_num = compound_match.group(1)
        if base_num and base_num in zh_num_map:
            return zh_num_map[base_num] + 0.5
        elif not base_num:  # 只有「半」
            return 0.5
    
    # 阿拉伯數字（包含小數）
    arabic_match = re.search(r"\d+\.?\d*", text)
    if arabic_match:
        return float(arabic_match.group())
    
    # 單純的「半」
    if text == "半":
        return 0.5
    
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

def _normalize_time_unit(unit_text: str) -> str:
    """標準化時間單位，統一轉換為分鐘"""
    # 從 USER_DEFINED_DICT 取得時間單位
    time_units = USER_DEFINED_DICT.get("_timeunit_", ["分", "分鐘", "小時"])
    
    # 單位對應表
    unit_map = {
        "分": "分鐘",
        "分鐘": "分鐘", 
        "小時": "小時",
        "時": "小時",
        "hr": "小時",
        "hour": "小時",
        "hours": "小時",
        "min": "分鐘",
        "mins": "分鐘",
        "minute": "分鐘",
        "minutes": "分鐘"
    }
    
    return unit_map.get(unit_text, unit_text)

def _convert_to_minutes(value: float, unit: str) -> int:
    """將時間轉換為分鐘"""
    if unit == "小時":
        return int(value * 60)
    else:  # 預設為分鐘
        return int(value)

def _validate_time_range(minutes: int) -> bool:
    """驗證時間範圍：5-300分鐘（5小時）"""
    return 5 <= minutes <= 300

def _extract_time_info(args_list, input_text):
    """
    提取時間資訊
    回傳: (time_data, intent_type)
    """
    combined_text = "".join(args_list) + input_text
    
    # 取得時間單位列表
    time_units = USER_DEFINED_DICT.get("_timeunit_", ["分", "分鐘", "小時"])
    
    # 優先級1: 尋找 數字+單位 組合
    for i, arg in enumerate(args_list):
        # 先嘗試提取數字
        time_value = _extract_number_zh(arg)
        if time_value and time_value > 0:
            # 尋找對應的時間單位
            time_unit = None
            
            # 檢查同一個 arg 是否包含單位
            for unit in time_units:
                if unit in arg:
                    time_unit = _normalize_time_unit(unit)
                    break
            
            # 檢查後續的 args
            if not time_unit and i + 1 < len(args_list):
                next_arg = args_list[i + 1]
                for unit in time_units:
                    if unit in next_arg:
                        time_unit = _normalize_time_unit(unit)
                        break
            
            # 檢查整個 input_text
            if not time_unit:
                for unit in time_units:
                    if unit in input_text:
                        time_unit = _normalize_time_unit(unit)
                        break
            
            # 如果找到數字但沒找到單位，預設為分鐘
            if not time_unit:
                time_unit = "分鐘"
            
            # 轉換為分鐘並驗證
            total_minutes = _convert_to_minutes(time_value, time_unit)
            
            if _validate_time_range(total_minutes):
                return {
                    "value": total_minutes,
                    "unit": "分鐘", 
                    "display": f"{total_minutes}分鐘",
                    "original": f"{time_value}{time_unit}"
                }, "time_explicit"
            else:
                # 超出範圍
                return None, "unknown"
    
    # 優先級2: 模糊時間表達
    vague_time_keywords = [
        "快速", "很快", "超快", "急", "馬上", "立刻", "現在", "趕時間", "越快越好",
        "慢慢", "不急", "充裕", "簡單", "容易", "輕鬆",
        "不限時間", "時間不限", "沒有時間限制", "有充裕時間",
        "中午", "晚餐", "等一下", "待會", "稍後"
    ]
    
    for keyword in vague_time_keywords:
        if keyword in combined_text:
            return input_text, "time_vague"
    
    # 優先級3: 檢查是否時間相關（用於 unknown 判斷）
    time_related_keywords = ["時間", "分", "小時", "快", "慢", "急", "等", "馬上", "立刻"]
    
    if any(keyword in input_text for keyword in time_related_keywords):
        return input_text, "time_vague"
    
    return None, "unknown"

def _has_time_relevance(args_list, input_text):
    """檢查輸入是否與時間相關"""
    
    time_related = [
        "時間", "分", "分鐘", "小時", "快", "慢", "急", "等", "馬上", "立刻", 
        "現在", "等一下", "待會", "中午", "晚餐", "簡單", "容易",
        "不限", "充裕", "趕", "越快越好"
    ]
    
    return any(keyword in input_text for keyword in time_related)

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern="", toolkitDICT={}):
    """time_limit intent 主要處理函數"""
    debugInfo(inputSTR, utterance)
    
    # 提取時間資訊
    time_data, intent_type = _extract_time_info(args, inputSTR)
    
    if intent_type == "time_explicit":
        # 成功提取到明確時間
        resultDICT["intent"] = "time_input"
        resultDICT["time_limit"] = time_data
        
    elif intent_type == "time_vague":
        # 模糊時間表達
        resultDICT["intent"] = "time_input"  
        resultDICT["time_limit"] = {
            "type": "vague",
            "description": time_data
        }
        
    else:  # intent_type == "unknown"
        # 檢查是否與時間相關
        if _has_time_relevance(args, inputSTR):
            resultDICT["intent"] = "time_clarification"
        else:
            resultDICT["intent"] = "unknown"
    
    return resultDICT


if __name__ == "__main__":
    """測試"""
    from pprint import pprint
    
    test_cases = [
        # 明確時間 - 正常情況
        ("三十分鐘", "[三十]分鐘", ["三十"]),
        ("30分鐘", "[30]分鐘", ["30"]),
        ("一小時", "[一]小時", ["一"]),
        ("半小時", "半小時", ["半小時"]),
        ("一個半小時", "[一個半]小時", ["一個半"]),
        ("兩個半小時", "[兩個半]小時", ["兩個半"]),
        
        # 明確時間 - 邊界測試  
        ("5分鐘", "[5]分鐘", ["5"]),        # 下限
        ("300分鐘", "[300]分鐘", ["300"]),  # 上限
        ("3分鐘", "[3]分鐘", ["3"]),        # 低於下限
        ("400分鐘", "[400]分鐘", ["400"]),  # 高於上限
        ("0分鐘", "[0]分鐘", ["0"]),        # 無效值
        
        # 單位變化
        ("三十分", "[三十]分", ["三十"]),     # 「分」vs「分鐘」
        ("2小時", "[2]小時", ["2"]),
        ("1.5小時", "[1.5]小時", ["1.5"]),  # 小數
        
        # 模糊時間表達
        ("快速料理", "[快速]料理", ["快速"]),
        ("慢慢來", "[慢慢]來", ["慢慢"]),
        ("不限時間", "不限時間", ["不限時間"]),
        ("很急", "很急", ["很急"]),
        ("中午要吃", "[中午]要吃", ["中午"]),
        ("簡單的料理", "[簡單]的料理", ["簡單"]),
        
        # 無關輸入
        ("今天天氣真好", "今天天氣真好", ["今天", "天氣", "真好"]),
        ("我餓了", "我餓了", ["我", "餓", "了"]),
        
        # 複雜情況
        ("大概30分鐘左右", "[大概][30]分鐘[左右]", ["大概", "30", "左右"]),
        ("最好十分鐘內", "[最好][十]分鐘[內]", ["最好", "十", "內"]),
    ]
    
    print("=== Time_limit Intent 測試 ===")
    for inputSTR, utterance, args in test_cases:
        resultDICT = {}
        result = getResult(inputSTR, utterance, args, resultDICT, {})
        
        print(f"\n輸入: {inputSTR}")
        print(f"結果: {result}")
        
        # 簡化顯示
        if result.get("intent") == "time_input":
            time_limit = result.get("time_limit", {})
            if "value" in time_limit:
                print(f"  → 明確時間: {time_limit['display']} (原始: {time_limit.get('original', 'N/A')})")
            elif "description" in time_limit:
                print(f"  → 模糊時間: {time_limit['description']}")
        elif result.get("intent") == "time_clarification":
            print(f"  → 需要澄清時間需求")
        elif result.get("intent") == "unknown":
            print(f"  → 無關輸入")