#!/user/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import logging
import pandas as pd
from random import choice
from datetime import datetime

import ingredientBot as iB

inSeasonDICT = json.load(open("./info/inSeason.json", encoding="utf-8")) 
IngredientRelatedDICT = json.load(open("./info/ingredient.json", encoding="utf-8"))

from ArticutAPI import ArticutAPI
articut = ArticutAPI.Articut()

inputSTR = "有什麼水果"

resultDICT = articut.parse(inputSTR, level="lv1")["result_pos"]

print(resultDICT[0])

pattern = "(?<!</FUNC_negation>)<VERB_P>[^<不]*?有[^<不]*?</VERB_P><CLAUSE_WhatQ>[^<]*?</CLAUSE_WhatQ><ENTITY_UserDefined>[^<]*?</ENTITY_UserDefined>"

print(re.match(pattern, resultDICT[0]))