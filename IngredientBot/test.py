from ArticutAPI import Articut
from datetime import datetime
import json
import re


"""
accountDICT = json.load(open("./account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])


#a = str(datetime.strptime(articut.parse("九月十號", level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
#print(a)

b = articut.parse("九月", level = "lv1")
print(b)

c = articut.parse("九月十號", level = "lv1")
print(c)

d = articut.parse("夏天", level = "lv1")
print(d)

e = articut.parse("今年夏天", level = "lv1")
print(e)

posSTR = "".join(c["result_pos"])

for g in re.finditer("<TIME_season>([^<]+)</TIME_season>", posSTR):
    print(g.group(1))

for g in re.finditer("<TIME_month>([^<]+)</TIME_month>", posSTR):
    print(g.group(1))


f = articut.parse("夏天", level = "lv3")
print(f)


a = articut.parse("九月", level = "lv")["time"]
print(a)

"""

if "bot" in "bot點名":
    print("yes")
else:
    print("no")

if "bot點名" in "bot點名":
    print("yes11")
else:
    print("no11")

if "bot點名123" in "bot點名":
    print("yes2")
else:
    print("no2")