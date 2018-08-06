# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# ﻿Пример выходного файла:
# ff
# dde
# c
# ab
import os

with open("Tests\dataset_24465_4.txt", "r") as f_in, open("Tests\out.txt", 'w') as f_out:
    lines = []
    for line in f_in:
        lines.append(line)

    f_out.write("".join(lines[::-1]))

d = []
for cur_dir, dirs, files in os.walk("main"):
    for file in files:
        if file[-3:] == ".py":
            if cur_dir not in d:
                d.append(cur_dir)
                print(cur_dir)
