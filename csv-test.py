import os
import csv
import time


local_date = time.strftime(
    "%Y", time.localtime())
local_day = time.strftime(
    "%m%d", time.localtime())
local_time = time.strftime(
    "_%H-%M-%S", time.localtime())
path = "./output-csv" + "/" + str(local_date) + "/" + str(local_day)

if not os.path.isdir(path):
    # os.mkdir  # 建立目錄(只能一次建立一層)
    os.makedirs(path)  # 多層次建立目錄
    with open(path + '/' + str(local_date + local_day + local_time) + '.csv', 'w') as csvfile:
        data = 'csv test file test!!'
        csvfile.write(data)
        print('context: {}'.format(data))
else:
    with open(path + '/' + str(local_date + local_day + local_time) + '.csv', 'w') as csvfile:
        data = 'csv test file test!!'
        csvfile.write(data)
        print('context: {}'.format(data))
