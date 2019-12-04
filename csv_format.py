import csv

with open('./jamesbond.csv') as csvfile:
    data = csv.reader(csvfile)
    passheader = next(data)
    for row in data:
        print(row)
