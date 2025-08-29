import json
import re
from requests import post
import ast
with open("./RSBot/account.info", encoding="utf-8") as f: #讀取account.info
        ACCOUNT_DICT = json.loads(f.read())

def getLLM(system="", assistant="", user=""):
    # print(system, assistant, user)
    resultSTR = ""
    
    if ACCOUNT_DICT["chatbot_prompt"]:
        url = f"{ACCOUNT_DICT['server']}/Loki_EN/Call/"
        payload = {
            "username": ACCOUNT_DICT["username"],
            "loki_key": ACCOUNT_DICT["loki_key"],
            "intent": list(ACCOUNT_DICT["chatbot_prompt"])[0],
            "func": "run_alias",
            "data": {
                "messages": []
            }
        }
        
        if system:
            payload["data"]["messages"].append({"role": "system", "content": system})
        if assistant:
            payload["data"]["messages"].append({"role": "assistant", "content": assistant})
        if user:
            payload["data"]["messages"].append({"role": "user", "content": user})
        if payload["data"]["messages"]:
            # print(payload["data"]["messages"])
            try:
                result = post(url, json=payload).json()
                # print(result)
                if result["status"]:
                    resultSTR = result["result_list"][0]["message"]["content"]
                else:
                    print(f"[getLLM] {result['msg']}")
            except Exception as e:
                print(f"[getLLM] {str(e)}")

    return resultSTR

def read_json_file(file_path):
    """Read a JSON file and return its content."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def find_item(brand_LIST, category):
    database_path = "./newlaptops.json"
    databaseDICT = read_json_file(database_path)
    item_in_brand = []
    item_in_category = []
    for brand in brand_LIST:
        if brand in databaseDICT["brand"].keys():
            if databaseDICT["brand"][brand] != []:
                item_in_brand = databaseDICT["brand"][brand]
                break
    if category in databaseDICT["category"].keys():
        if databaseDICT["category"][category] != []:
            item_in_category = databaseDICT["category"][category]
    final_item = list(set(item_in_brand) & set(item_in_category))
    if final_item == []:
        if item_in_brand == [] and item_in_category == []:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            return f"We don't provide any {",".join(brand_LIST)} laptop."
        elif item_in_brand != []:
            final_item = item_in_brand
        elif item_in_category != []:
            final_item = item_in_category
    idx = 5
    if len(final_item) < 5:
        idx = len(final_item)
    return f"""
            We find those items meet your needs.
Brand: {brand}
Purpose: {category}
+ {"\n+ ".join(final_item[:idx])}
            """ 

def check_if_brand(check_brand_LIST):
    brand_path = "./RSBot/intent/USER_DEFINED.json"
    data = read_json_file(brand_path)
    check_brand_LIST = [x.lower() for x in check_brand_LIST]
    brand_LIST = [x.lower() for x in data["__brandname__"]]
    new_brand_LIST = list(set(check_brand_LIST) & set(brand_LIST))
    return new_brand_LIST

def get_goal_classify(goal):
    system =  ""
    assistant =  """
   Based on the goal. which category of laptop meet the customer's need
   Category:
   Home / Personal
   Gaming
   Work / Business
   Content Creation
   Education

   Give me list with format 
   ["category"]
   """
    user = "A laptop for"+goal
    resSTR = getLLM(system, assistant, user)
    # print(resSTR)
    match = re.search(r'\[.*?\]', resSTR)
    if match:
        cate_LIST = ast.literal_eval(match.group())
        cate = cate_LIST[0]
        return cate
    return ""

def get_item(final_refDICT):

    if final_refDICT['items'] != []:
        item = final_refDICT["items"][-1]
    if final_refDICT["brand"] != []:
        feature = ""
        new_brand_LIST = check_if_brand(final_refDICT["brand"])
        if new_brand_LIST == []:
            return f"I can't find this brand. Can you say again?"
        
    if final_refDICT["goal"] != []:
        goal = final_refDICT["goal"][-1]
        category = get_goal_classify(goal)
    
    r_item = find_item(new_brand_LIST, category)
    return r_item

def reply_maker(final_refDICT):
    key_list = ["items", "brand", "goal"]
    for key_ in key_list:
        if key_ not in final_refDICT:
            final_refDICT[key_] = []        
    if final_refDICT["items"] == []:
        replySTR = "What would you want to buy?"
    elif final_refDICT["brand"] == []:
        replySTR = "Which brand do you want?"
    elif final_refDICT["goal"] == []:
        replySTR = "What you’ll mainly use it for?"
    else:
        replySTR = get_item(final_refDICT)

    return replySTR

if __name__ == "__main__":
    pass