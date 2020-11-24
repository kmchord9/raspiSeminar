# -*- coding: utf-8 -*-

import csv
import datetime

def saveCSV(time, data, save_path="./datalog/"):

    now_str = datetime.datetime.now().strftime("%Y%m%d")
    filename = save_path + now_str + ".csv"

    with open(filename, 'a') as f:
        strTime = time.strftime("%Y/%m/%d %H:%M:%S")
        addStr = strTime + "\t" + str(data)
        
        print(addStr, file=f)




