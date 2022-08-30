#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki Template For Python3

    [URL] https://nlu.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""
try:
    import rapidjson as json
except:
    import json
import math
from requests import post
from requests import codes
import sympy

try:
    from intent import Loki_dividend
    from intent import Loki_postve_num
    from intent import Loki_divisor
    from intent import Loki_quest_goal
    from intent import Loki_multiplicand
    from intent import Loki_multiplier
    from intent import Loki_negtve_num
    from intent import Loki_bg_setting
except:
    #from .intent import Loki_dividend
    from .intent import Loki_postve_num
    from .intent import Loki_divisor
    from .intent import Loki_quest_goal
    from .intent import Loki_multiplicand
    from .intent import Loki_multiplier
    from .intent import Loki_negtve_num
    from .intent import Loki_bg_setting

from pprint import pprint

accountDICT = json.load(open("account.info", encoding="utf-8"))
LOKI_URL = "https://nlu.droidtown.co/Loki/BulkAPI/"
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki_key"]
# Filter descrption
# INTENT_FILTER = []        => All intents (Default)
# INTENT_FILTER = [intentN] => Only use intent of INTENT_FILTER
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.lokiResultLIST = []
        # Default: INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {"intentLIST":[],
                  "symbolLIST":[],
                  "symbolDICT":{},
                  "eqLIST":[],
                  "questGoalLIST":[],
                  "ansLIST":[],
                  "inputStrLIST":[]
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # dividend
                if lokiRst.getIntent(index, resultIndex) == "dividend":
                    resultDICT = Loki_dividend.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # postve_num
                if lokiRst.getIntent(index, resultIndex) == "postve_num":
                    resultDICT = Loki_postve_num.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # divisor
                if lokiRst.getIntent(index, resultIndex) == "divisor":
                    resultDICT = Loki_divisor.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # quest_goal
                if lokiRst.getIntent(index, resultIndex) == "quest_goal":
                    resultDICT = Loki_quest_goal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # multiplicand
                if lokiRst.getIntent(index, resultIndex) == "multiplicand":
                    resultDICT = Loki_multiplicand.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # multiplier
                if lokiRst.getIntent(index, resultIndex) == "multiplier":
                    resultDICT = Loki_multiplier.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # negtve_num
                if lokiRst.getIntent(index, resultIndex) == "negtve_num":
                    resultDICT = Loki_negtve_num.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # bg_setting
                if lokiRst.getIntent(index, resultIndex) == "bg_setting":
                    resultDICT = Loki_bg_setting.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # dividend
    print("[TEST] dividend")
    inputLIST = ["""The school has $20,000""","""you have 4 pieces of candy split evenly into 2 bags""","""Melissa buys 2 packs of tennis balls for $12 in total""","""you have 80 tickets for the fair and each ride costs 5 tickets"""]
    testLoki(inputLIST, ['dividend'])
    print("")

    # postve_num
    print("[TEST] postve_num")
    inputLIST = ["""Billy had 2 books""","""He then bought 1 book""","""Adrianna has 10 pieces""","""there are 6 tennis balls""","""1 of her shots went in the hoop""","""Ashley bought a big bag of candy""","""In one box, there are 6 music books""","""Melissa buys 2 packs of tennis balls""","""There are 6 chef assistants and 2 servers""","""Together with the 5 guitars that the store has""","""He went to the library to take out 2 more books""","""There are 8 guitars and 3 flutes from the order""","""On top of each row, there is a stack of 6 bricks""","""Next to the 3 juice fountains, there are 5 tables""","""restaurant receives a shipment of 86 veal cutlets""","""she went to the store to get 3 more pieces of gum""","""On the other side of the cafeteria, there are 7 tables""","""The restaurant has 175 normal chairs and 20 chairs for babies""","""There are 4 violins in the store room and 3 violins on display""","""A bricklayer stacks bricks in 2 rows, with 10 bricks in each row""","""The bag had 102 blue candies, 100 red candies and 94 green candies""","""There are 9 pots of cream of mushroom and 8 pots of vegetable soup""","""she went to the store and got 70 pieces of strawberry gum and 10 pieces of bubble gum""","""there are 4 stacks of chocolate puddings, 7 stacks of brownies, and 5 stacks of pasta salad"""]
    testLoki(inputLIST, ['postve_num'])
    print("")

    # divisor
    print("[TEST] divisor")
    inputLIST = ["""there are 6 tennis balls""","""each piece of equipment costs $50""","""Melissa buys 2 packs of tennis balls""","""you have 4 pieces of candy split evenly into 2 bags""","""you have 80 tickets for the fair and each ride costs 5 tickets"""]
    testLoki(inputLIST, ['divisor'])
    print("")

    # quest_goal
    print("[TEST] quest_goal")
    inputLIST = ["""How many cookies did you sell""","""How many pots of soup are there?""","""How many staff are working there?""","""How many books does Billy have now""","""How many levels did Shara complete?""","""How many shots were there in total?""","""How many tables are there in total?""","""How many candies were there in total""","""How many guitars are there in total?""","""How many violins are there in total?""","""How many candies does Andie have now?""","""How many headphones are in the store?""","""How many stacks of dessert are there?""","""How many music books are there in total?""","""How many trumpets did he order in total?""","""How many words were on the spelling test?""","""How many pieces of gum does Adrianna have now""","""how many trading cards did the hobby store sell""","""How many chairs does the restaurant have in total"""]
    testLoki(inputLIST, ['quest_goal'])
    print("")

    # multiplicand
    print("[TEST] multiplicand")
    inputLIST = ["""A bricklayer stacks bricks in 2 rows, with 10 bricks in each row"""]
    testLoki(inputLIST, ['multiplicand'])
    print("")

    # multiplier
    print("[TEST] multiplier")
    inputLIST = ["""On top of each row, there is a stack of 6 bricks""","""A bricklayer stacks bricks in 2 rows, with 10 bricks in each row"""]
    testLoki(inputLIST, ['multiplier'])
    print("")

    # negtve_num
    print("[TEST] negtve_num")
    inputLIST = ["""there was 1 word misspelled""","""2 of her shots did not go in the hoop""","""Shara shared 3 candies with her friend""","""A customer comes in to return 2 pairs of headphones""","""you sold 320 chocolate cookies and 270 vanilla cookies""","""the hobby store sold 15,498 more trading cards than normal""","""The hobby store normally sells 10,576 trading cards per month"""]
    testLoki(inputLIST, ['negtve_num'])
    print("")

    # bg_setting
    print("[TEST] bg_setting")
    inputLIST = ["""Find two numbers""","""There wasn’t enough gum""","""Ariel was playing basketball""","""if it takes 3 cutlets to make a dish"""]
    testLoki(inputLIST, ['bg_setting'])
    print("")


if __name__ == "__main__":
    # Test all intents
    #testIntent()

    inputLIST = ["Charlene had a pack of 35 pencil crayons",
                 "She gave 6 to Theresa",
                 "She gave 3 to her friend Mandy",
                 "How many pencil crayons does Charlene have left?"
                ]

    inputLIST = ["There were 3 pizzas in total at the pizza shop",
                 "A customer bought 1 pizza.",
                 "How many pizzas are left?"
                ]

    inputLIST = ["Your friend said she had 11 stickers",
                 "When you helped her clean her desk",
                 "she only had a total of 10 stickers",
                 "How many stickers are missing?"
                ]

    inputLIST = ["Adrianna has 100 pieces of gum to share with her friends",
                 "When she went to the park",
                 "she shared 10 pieces of strawberry gum",
                 "When she left the park",
                 "Adrianna shared another 10 pieces of bubble gum",
                 "How many pieces of gum does Adrianna have now?"
                ]

    inputLIST = ["Your team scored a total of 123 points",
                 "67 points were scored in the first half",
                 "How many were scored in the second half?"
                ]

    inputLIST = ["Nathan has a big ant farm",
                 "He decided to sell some of his ants",
                 "He started with 965 ants",
                 "He sold 213. How many ants does he have now?"
                 ]

    inputLIST = ["The hobby store normally sells 10,576 trading cards per month",
                 "In July",
                 "the hobby store sold a total of 20,777 trading cards",
                 "How many more trading cards did the hobby store sell in July compared with a normal month?"]

    #inputLIST = ["A bricklayer stacks bricks in 2 rows",
    #             "with 10 bricks in each row",
    #             "How many bricks are there in total?"]

    #problems are labeled the same in Loki_postve_num.py

    #1st problem
    #status: working
    #inputLIST = ["A new order of instruments comes in today.",
    #             "There are 8 guitars and 3 flutes from the order.",
    #             "And together with the 5 guitars that the store has,",
    #             "how many flutes are there in total?"]

    #2nd problem
    #status: working
    #inputLIST = ["Next to the 3 juice fountains",
    #             "there are 5 tables.",
    #             "On the other side of the cafeteria",
    #             "there are 7 tables.",
    #             "How many tables are there in total?"]


    #3rd problem
    #status: working
    #inputLIST = ["Adrianna has 10 pieces of gum to share with her friends.",
                 #"There wasn’t enough gum for all her friends,",
                 #"so she went to the store to get 3 more pieces of gum",
                 #"How many pieces of gum does Adrianna have now?"]

    #inputLIST = ["Allen has 2 boxes of paper to print his works.",
                 #"There wasn’t enough paper for the printing,",
                 #"so he went to the bookshop to get 6 more boxes of paper",
                 #"How many boxes of paper does Allen have now?"]

    #4th problem
    #status: working
    #inputLIST = ["Billy had 2 books at home.",
                 #"He went to the library to take out 2 more books.",
                 #"He then bought 1 book.",
                 #"How many books does Billy have now?"]

    #5th problem
    #status: working
    inputLIST = ["The restaurant has 175 normal chairs and 20 chairs for babies.",
                 "How many chairs does the restaurant have in total?"]

    #6th problem
    #status: working
    #handles the case if all 3 are not the same
    #inputLIST = ["Ashley bought a big bag of candy.",
                 #"The bag had 102 blue candies",
                 #"100 red candies and 94 green candies.",
                 #"How many candies were there in total?"]

    #7th problem
    #status: working
    #inputLIST = ["There are 4 classic violins in the store room and 3 modern violins on display.",
                 #"How many violins are there in total?"]

    #8th problems
    #status: not working
    #issue: KeyError: piece_of_gum
    #inputLIST = ["Adrianna has 10 pieces of gum to share with her friends.",
                 #"There wasn’t enough gum for all her friends",
                 #"so she went to the store and got 70 pieces of strawberry gum and 10 pieces of bubble gum.",
                 #"How many pieces of gum does Adrianna have now?"]

    #Test multiplication
    #status: working
    #inputLIST = ["A clothing company has 4 different kinds of sweatshirts.",
                 #"Each year, the company makes 60,000 of each kind of sweatshirt.",
                 #"How many sweatshirts does the company make each year?"]

    #10th problem
    #status: not working
    #issue: quest goal is correct, but user defined dict appends "cream of mushroom" instead of soup into SymboDict
    #inputLIST = ["There are 9 pots of cream of mushroom and 8 pots of vegetable soup.",
                 #"How many pots of soup are there?"]

    #9th problem
    #status: not working
    #test if loki recognizes background info
    #issue: Loki recognizes assistants and servers as assistant_0 and 1
    #quest goal is "staff"
    inputLIST = ["There are 6 chef staff and 2 staff.",
                 "How many staff are working there?"]

    #inputLIST = ["A garden has 52 rows and 15 columns of bean plants",
                 #"How many plants are there in all?"]



    #inputLIST = ["The sum of two numbers is twenty-three",
                 #"and the larger number is five more than the smaller number",
                 #"Find these numbers"]

    #inputLIST = ["A number is 12 less than another",
    #             "The sum of the numbers is 28",
    #             "find the Numbers"]

    #inputLIST = ["the sum of the digits of a two digit number is 15.",
    #             "if the digits are interchanged the result exceeds the original number by 9",
    #             "find the number."]

    #inputLIST = ["Lastly",
    #             "Rob compared Canada’s CN Tower and Seattle’s Space Needle.",
    #             "How tall is the Space Needle if the CN Tower stands at 553 meters high",
    #             "and it is taller than the Space Needle by 369 meters?"
    #]

    #inputLIST = ["If you have 4 pieces of candy split evenly into 2 bags",
    #             "how many pieces of candy are in each bag?"]

    #inputLIST = ["If you have 80 tickets for the fair and each ride costs 5 tickets",
                 #"how many rides can you go on?"]

    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    pprint(resultDICT)

    print("\n\n====\nQuestion: {}".format(", ".join(inputLIST)))
    #check symbols
    if resultDICT["eqLIST"] != []:
        print("# Equations:{}".format(resultDICT["eqLIST"]))
    else:
        print("#  Symbols:{}".format(resultDICT["symbolDICT"]))
    #check quest goal
    print("# Quest toal:{}".format(resultDICT["questGoalLIST"]))

    for intent in resultDICT["intentLIST"]:
        if intent == "simulEq":
            try:
                answerDICT = sympy.solve(resultDICT["eqLIST"], resultDICT["symbolLIST"])
                print("answer = {}".format(answerDICT))
            except:
                print("Sorry...I can't solve them...")

        elif intent == "addition":
            if resultDICT["eqLIST"] == []:
                #ans=sympy.Symbol("ans")
                for goal in resultDICT["questGoalLIST"]:
                    if goal in resultDICT["symbolDICT"].keys():
                        #code for printing out equation in string form
                        equation = ''
                        for var,val in resultDICT["symbolDICT"][goal]:
                            #if(var == resultDICT["symbolDICT"][goal][-1][0]):
                                #equation = equation + var.name
                            #else:
                            equation = equation + var.name + " + "
                        equation = equation.rstrip(" + ")
                        print("answer = {}".format(equation))
                    else:
                        print("I don't know. I don't see {} mentioned anywhere.".format(goal))
                #evaluate previous str equation as math equation
                try:
                    expr = sympy.sympify(equation)
                    print("answer = {}".format(expr.subs(resultDICT["symbolDICT"][goal])))
                except NameError:
                    pass
            else:
                try:
                    answerDICT = sympy.solve(resultDICT["eqLIST"], resultDICT["symbolLIST"])
                    print("answer = {}".format(answerDICT))
                except:
                    print("Cannot find a reasonable solution to equations:")
                    print(resultDICT["eqLIST"])
        elif intent == "multiply":
            for goal in resultDICT["questGoalLIST"]:
                if goal in resultDICT["symbolDICT"].keys():
                    equation = ""
                    for k in resultDICT["symbolDICT"].keys():
                        for v in resultDICT["symbolDICT"][k]:
                            var = v[0]
                            equation = equation + var.name + " * "
                            resultDICT["eqLIST"].append(v)
                    equation = equation.rstrip(" * ")
                    print("answer = {}".format(equation))
                else:
                    print("I don't know. I don't see {} mentioned anywhere.".format(goal))
                try:
                    #evaluate previous str equation as math equation
                    expr = sympy.sympify(equation)
                    print("answer = {}".format(expr.subs(resultDICT["eqLIST"])))
                except NameError:
                    pass
        elif intent == "subtraction":
            equation = ""
            for k in resultDICT["symbolDICT"].keys():
                for v in resultDICT["symbolDICT"][k]:
                    var = v[0]
                    equation = equation + var.name + " + "
                    resultDICT["eqLIST"].append(v)
            equation = equation.rstrip(" + ")
            print("answer = {}".format(equation))

            # add abs to ensure positive result
            expr = sympy.sympify(equation)
            print("answer = {}".format(abs(expr.subs(resultDICT["eqLIST"]))))
        elif intent == "division":
            pass


    #print("Result =>")
    #pprint(resultDICT)