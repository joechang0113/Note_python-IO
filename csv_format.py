import csv

with open('./jamesbond.csv') as csvfile:
    # 每一列的 list 直接輸出
    # data = csv.reader(csvfile)
    # passheader = next(data)
    # for row in data:
    #     print(row)

    # 讀取後，轉為 Python 的 dictionary 格式
    data = csv.DictReader(csvfile)
    for row in data:
        print(row['Film'], row['Year'], row['Actor'],
              row['Director'], row['Box Office'], row['Budget'], row['Bond Actor Salary'],)
