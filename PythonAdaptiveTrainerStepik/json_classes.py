# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# ﻿Эквивалент на Python:
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно
# от одного класса более одного раза.Для каждого класса вычислите предком скольких классов он является и выведите эту
# информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.
# Sample Input:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
#
# Sample Output:
# A : 3
# B : 1
# C : 2

import json


def check(start, target):
    O = []
    C = []
    [O.append(node) for node in classes[start]]
    C.append(start)
    while len(O)> 0:
        if O[0] == target:
            return True
            break
        else:
            cur = O.pop(0)
            C.append(cur)
            for node in classes[cur]:
                if node not in C:
                    O.append(node)
    else:
        return False


description = json.loads('''[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]},
                          {"name": "A", "parents": []}, {"name": "D", "parents": ["C", "F"]},
                          {"name": "E", "parents": ["D"]}, {"name": "F", "parents": []}]''')
classes = dict()
for item in description:
    classes[item['name']] = item['parents']

for name_out in sorted(classes):
    count = 1
    for name_in in classes:
        if check(name_in, name_out):
            count += 1
    print("{} : {}".format(name_out, count))
