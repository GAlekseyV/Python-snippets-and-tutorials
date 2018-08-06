# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv
import os

filename = os.path.join("Tests", "Crimes.csv")
crimes = dict()

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Primary Type'])
        if row["Primary Type"] not in crimes:
            crimes[row["Primary Type"]] = 1
        else:
            crimes[row["Primary Type"]] += 1

print(sorted(crimes.items(), key=lambda v: v[1]))