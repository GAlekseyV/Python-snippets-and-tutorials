# Напишите программу, которая считывает текст из файла
# (в файле может быть больше одной строки) и выводит самое
# частое слово в этом тексте и через пробел то, сколько раз
# оно встретилось. Если таких слов несколько, вывести лексикографически
# первое (можно использовать оператор < для строк).
#
# Слова, написанные в разных регистрах, считаются одинаковыми.

import os

name = os.path.join('Tests', 'dataset_3363_3.txt')
words = {}
with open(name, 'r') as f:
    for line in f:
        for word in line.lower().strip().split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

for word, count in words.items():
    if words[word] == max(words.values()):
        print(word, count)


    # with open('data_out.txt', 'w') as f:
#     f.write(str_out)
