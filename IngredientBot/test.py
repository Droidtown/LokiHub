import json

inSeasonDICT = json.load(open("./info/inSeason.json", encoding="utf-8"))


li=[]
for month in inSeasonDICT.keys():
    print(month)
    li = li + inSeasonDICT[month]["海鮮"]+inSeasonDICT[month]["蔬菜"]+inSeasonDICT[month]["水果"]

print(len(list(set(li))))


        

        