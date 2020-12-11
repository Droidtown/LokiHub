import csv
f = open("currency_CE.csv","r")
reader = csv.reader(f)
curDICT = {}
for row in reader:
    curDICT[row[0]]=[row[1]]
print(curDICT)

    



