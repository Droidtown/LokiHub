import pandas as pd
import re

gymsInfo = pd.read_csv('data/climbingGym.csv', encoding = 'utf-8')

#print(gymsInfo.iloc[:,13])
print(gymsInfo.iloc[:,0])
#print(type(gymsInfo))

print(re.search("紅石", str(gymsInfo.iloc[:,0])))
print("紅石" in str(gymsInfo.iloc[:,0]))