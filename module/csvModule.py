# -*- coding: utf-8 -*-

import csv
import datetime
import os
'''
def saveCSV(time, data, save_path="./datalog/"):

    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"

    with open(filename, 'a') as f:
        strTime = time.strftime("%Y/%m/%d %H:%M:%S")
        addStr = strTime + "\t" + str(data)
        
        print(addStr, file=f)
'''
def fileExistCheckAndSaveCsv(time, value, savePath="./datalog/"):
    '''
    今日の日付のcsvファイルの存在を確認して、引数のデータをcsvに保存する

    引数
      time 　　： datetime型 (保存時間)
      value　　： 任意のリテラル (センサーデータなど)
      savePath ： csvの保存先デフォルトではdatalogのフォルダ

    戻値（boolean型）
    　今日の日付のcsvファイルが
       存在するとき　　：　True
       存在しないとき　：　False　

    '''


    strNow = datetime.datetime.now().strftime("%Y%m%d")
    filePath = savePath + strNow + ".csv"

    def valueSaveToCsv(time, value, savePath):
        with open(filePath, 'a') as f:
            strTime = time.strftime("%Y/%m/%d %H:%M:%S")
            txtData = strTime + "\t" + str(value)
            
            print(txtData, file=f)

    if os.path.isfile(filePath):
        valueSaveToCsv(time, value, savePath)

        return True

    else:
        valueSaveToCsv(time, value, savePath)

        return False




    


