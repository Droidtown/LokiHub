#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
名稱： Loki Intent Update Tool
作者： Droidtown
日期： 2022-02-22
信箱： info@droidtown.co
範例： Updater.py -o <old_intent(s)_dir> -n <new_intent(s)_dir>
說明： Updater.py 會將 <old_intent(s)_dir> 目錄中檔名符合 Loki_ 開頭
      以及 .py 結尾的標準 Loki 意圖檔，和 <new_intent(s)_dir> 目錄中
      的同名檔案做比對。
      只要某個句型在新的意圖檔裡有，而舊的意圖檔裡沒有，就會產生出一個綜合了
      新舊句型的意圖檔供開發者參考。更新後的意圖檔將會加上 __updated 做為
      檔名後綴。在這個加上了 _updated 檔名後綴的檔案裡，靠近底部檔尾的地方
      ，則會列出所有「新」的句型。開發者只要把這個段落複製起來，貼入原有的意
      圖檔裡的對應段落，即完成更新。
      除了句型以外，Updater.py 也會更新全部意圖檔中的 userDefinedDICT
      使用者自訂義字典。
"""

from argparse import ArgumentParser
import json
import os

def utterance_updater(oldIntentDirectory="./", newIntentDirectory=None):
    resultBOOL = False
    if newIntentDirectory == None:
        return resultBOOL
    else:
        pass

    #收集舊的 intent 檔名
    oldIntentFileLIST = []
    for f in os.listdir("./"):
        if f.startswith("Loki_") and f.endswith(".py"):
            if f.endswith("_updated.py"):
                pass
            else:
                oldIntentFileLIST.append(f)
    oldIntentFileLIST.sort()

    for f in oldIntentFileLIST:
        print("[1] 檢查{}".format(f))
        #取出舊 intent 中的句型
        with open(f, encoding="utf-8") as intentFILE:
            oldIntentSrcLIST = intentFILE.readlines()
        while oldIntentSrcLIST[-1] == "\n":
            oldIntentSrcLIST = oldIntentSrcLIST[:-1]

        #取出新 intent 中的和舊 intent 同檔名的 .py 檔中的句型
        try:
            with open("{}/{}".format(newIntentDirectory, f), encoding="utf-8") as intentFILE:
                newIntentSrcLIST = intentFILE.readlines()
            while newIntentSrcLIST[-1] == "\n":
                newIntentSrcLIST = newIntentSrcLIST[:-1]
        except FileNotFoundError:
            pass

        #若新 intent 中的句型已存在於舊 intent 裡，pass；否則，如將該 intent 更新。
        updatedBOOL = False
        for n in newIntentSrcLIST:
            if n in oldIntentSrcLIST:
                pass
            else:
                if n.startswith("    if utterance == "):
                    print("    >>加入新句型判斷：{}".format(n))
                    updatedBOOL = True
                    oldIntentSrcLIST.insert(-2, "\n{}{}".format(n, "        # write your code here\n        pass\n"))
                else:
                    pass

        if updatedBOOL == True:
            with open(f.replace(".py", "_updated.py"), mode="w", encoding="utf-8") as updatedFILE:
                updatedFILE.write("".join(oldIntentSrcLIST))
            updatedBOOL = False
        else:
            print("    >>沒有新句型需要新增。")

    return resultBOOL

def userDefinedDICT_updater(oldIntentDirectory="./", newIntentDirectory=None):
    resultBOOL = False
    if newIntentDirectory == None:
        return resultBOOL
    else:
        pass

    #收集舊的 intent 檔名
    oldIntentFileLIST = []
    for f in os.listdir("./"):
        if f.startswith("Loki_") and f.endswith(".py"):
            if f.endswith("_updated.py"):
                pass
            else:
                oldIntentFileLIST.append(f)
    oldIntentFileLIST.sort()

    #取得新的 userDefinedDICT

    with open("{}/{}".format(newIntentDirectory, oldIntentFileLIST[0]), encoding="utf-8") as intentFILE:
        newIntentSrcLIST = intentFILE.readlines()
    for n in newIntentSrcLIST:
        if n.startswith("userDefinedDICT"):
            newUserDefinedDICT = n
            break


    for o in oldIntentFileLIST:
        print("[2] 更新 userDefinedDICT：{}".format(o))
        with open(o, encoding="utf-8") as intentFILE:
            oldIntentSrcLIST = intentFILE.readlines()
        for l in range(len(oldIntentSrcLIST)):
            if oldIntentSrcLIST[l].startswith("userDefinedDICT"):
                try: #這裡只是測試看看 intent 中的 userDefinedDICT 是否仍然列在同一行內，未經手動調整斷行。
                    json.loads(oldIntentSrcLIST[l].split("=")[1])
                except:
                    return False
                oldIntentSrcLIST[l] = newUserDefinedDICT
                break
            else:
                pass
        with open(o, mode="w", encoding="utf-8") as updatedFILE:
            updatedFILE.write("".join(oldIntentSrcLIST))

    return True

if __name__ == "__main__":
    progSTR = "Loki Intent Update Tool"
    usageSTR = "\nUpdater.py -o <old_intent(s)_dir> -n <new_intent(s)_dir>"
    descriptionSTR = """
    Updater.py 會將 <old_intent(s)_dir> 目錄中檔名符合 Loki_ 開頭
    以及 .py 結尾的標準 Loki 意圖檔，和 <new_intent(s)_dir> 目錄中
    的同名檔案做比對。

    只要某個句型在新的意圖檔裡有，而舊的意圖檔裡沒有，就會產生出一個綜合了
    新舊句型的意圖檔供開發者參考。更新後的意圖檔將會加上 __updated 做為
    檔名後綴。在這個加上了 _updated 檔名後綴的檔案裡，靠近底部檔尾的地方
    ，則會列出所有「新」的句型。開發者只要把這個段落複製起來，貼入原有的意
    圖檔裡的對應段落，即完成更新。

    除了句型以外，Updater.py 也會更新全部意圖檔中的 userDefinedDICT
    使用者自訂義字典。
    """
    argParser = ArgumentParser(prog=progSTR, usage=usageSTR, description=descriptionSTR, epilog=None)
    argParser.add_argument("-o", "--old-intent-dir", help="Old intent(s) directory", dest="oldIntentDirectory")
    argParser.add_argument("-n", "--new-intent-dir", help="New intent(s) directory", dest="newIntentDirectory")
    args = argParser.parse_args()

    #<manual_section>
    manualMode = True
    if manualMode == False:
        pass
    else:
        args.oldIntentDirectory = "./"
        args.newIntentDirectory = "./intent_new"
    #</manual_section>


    if None in (args.oldIntentDirectory, args.newIntentDirectory):
        argParser.print_help()
    else:
        print("舊 Intent 目錄：{}".format(args.oldIntentDirectory))
        print("新 Intent 目錄：{}".format(args.newIntentDirectory))
        if os.path.isdir(args.oldIntentDirectory):
            if os.path.isdir(args.newIntentDirectory):
                print("\n作業開始\n")
                if utterance_updater(oldIntentDirectory=args.oldIntentDirectory, newIntentDirectory=args.newIntentDirectory):
                    print("無法完成新句型檢查！")
                else:
                    print("完成句型新增檢查！")
                    print("請查看目錄中以 _updated.py 結尾的檔案末端以取得新的句型段落。")

                if userDefinedDICT_updater(oldIntentDirectory=args.oldIntentDirectory, newIntentDirectory=args.newIntentDirectory):
                    print("成功更新 userDefinedDICT")
                else:
                    print("更新 userDefinedDICT 失敗！")
            else:
                print("新 Intent 目錄：{} 不存在或不是合理的目錄路徑。".format(args.newIntentDirectory))
        else:
            print("舊 Intent 目錄：{} 不存在或不是合理的目錄路徑。".format(args.oldIntentDirectory))