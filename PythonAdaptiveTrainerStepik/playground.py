# put your python code here

# row_out = [[4, 4, 4, 4, 4]]
# print(len(row_out))
# print(len(row_out[0]))
#
# column_out = [[4], [4], [4], [4]]
# print(len(column_out))
# print(len(column_out[0]))
#
# one = [[1]]
# print(len(one))
# print(len(one))
#
# line = '1'
# matrix = []
# matrix.append([int(i) for i in line.split()])
# print(matrix)
#
#
# def update_dictionary(d, key, value):
#     # put your python code here
#     if key in d.keys():
#         d[key].append(value)
#     elif 2*key in d.keys():
#         d[2*key].append(value)
#     else:
#         d[2*key] = [value]
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}
import math
import sys
import requests
import os

# words = "a aa abC aa ac abc bcd a".lower().split()
# stat = {}
# for word in words:
#     if word in stat:
#         stat[word] += 1
#     else:
#         stat[word] = 1
#
# [print(key, value) for key, value in stat.items()]
#
# r = int(input())
# print(2 * math.pi * r)

# [print(arg, end=' ') for arg in sys.argv[1:]]

# name = os.path.join('Tests', 'dataset_3378_3.txt')
# url = ''
# end = False
# with open(name, 'r') as f:
#     url = f.readline().strip()
# r = requests.get(url)
# url = r.text.strip()
# text = url.split()
# print(text)
# while text[0] != "We":
#     r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/" + url)
#     url = r.text.strip()
#     text = url.split()
#     print(text)
# print(r.text)


# def s(a, *vs, b = 10):
#     res = a + b
#     for v in vs:
#         res += v
#     return res
#
#
# print(1 in [1, 2, 3])
#
#
# import datetime
# year, month, day = [int(x) for x in input().split()]
# cur_date = datetime.date(year, month, day)
# delta = datetime.timedelta(days = int(input()))
# new_date = cur_date + delta
# print(new_date.year, new_date.month, new_date.day, sep=" ")

import itertools


def primes():
    num = 2
    while True:
        isPrime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        if isPrime:
            yield num
        num += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
