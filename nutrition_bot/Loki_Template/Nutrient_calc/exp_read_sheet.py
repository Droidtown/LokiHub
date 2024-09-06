#!/user/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def age_matcher(n):
        if n < 4:
                return "1Y"
        elif n < 7: 
                return "4Y"
        elif n < 10:
                return "7Y"
        elif n < 13:
                return "10Y"
        elif n < 16:
                return "13Y"
        elif n < 19:
                return "16Y"
        elif n < 31:
                return "19Y"
        elif n < 51:
                return "31Y"
        elif n < 71:
                return "51Y"
        else:
                return "71Y"

def dri_matcher(age, gen, substance, kind):
        data = pd.read_excel(r'./dietary_reference_intakes.xlsx', header=1) 
        df = pd.DataFrame(data)
        if gen == "男":
                substance = gen + substance
        nu_total = ["維生素A", "維生素D", "維生素E", "維生素K", "維生素C", "維生素B1", "維生素B2", "菸鹼素", "維生素B6", "維生素B12", "葉酸", "鈣", "磷", "鎂", "鐵", "鋅", "碘", "鉀", "鈉"]
        a = df.where(df==age).dropna(how='all').dropna(axis=1)            #比對年齡、找row
        
        if kind:
                amount = float(df.loc[a.index, substance])                             #找column
                unit = df.loc[0, substance]                                          #找單位
                return amount, unit
        else:
                ret = {}
                for i in nu_total:
                        sub = i
                        if gen == "男":
                                sub = gen + i
                        amount = float(df.loc[a.index, sub])                            #找column
                        unit = df.loc[0, sub]                                          #找單位
                        #print(i,":", amount, unit)
                        ret[i] = str(amount) + unit
                return ret


def start_dri(age, gen, substance):
        age = age_matcher(int(age))                    # age in
        #gen = input("enter gender:")                                     # gender in
        if gen == "男" or gen == "男性" or gen == "男生" or gen == "生理男" or gen == "性別男":
                gen = "男"
        #substance = input("enter nutrient: ")                            # nutrient in
        kind = True
        if substance == "營養":
                kind = False                                                    # kind: [True = specific, False = all nutrients]
        if kind:
                return dri_matcher(age, gen, substance, kind)[0], dri_matcher(age, gen, substance, kind)[1]
                #print(substance, ":", dri_matcher(age, gen, substance, kind)[0], dri_matcher(age, gen, substance, kind)[1])
        else:
                ret = dri_matcher(age, gen, substance, kind)
                return ret
                #for ind, value in ret.items():
                        #return ind, value
                        #print(ind, ":", value)
                #print(substance, ":", dri_matcher(age, gen, substance, kind)[1], dri_matcher(age, gen, substance, kind)[2])
