# https://realpython.com/python-histograms/
# Histogramms in Pure Python
from collections import Counter
import random
random.seed(1)

vals = [1, 3, 4, 6, 8, 9, 10]
# Each number in 'vals' will occur between 5 and 15 times.
freq = (random.randint(5, 15) for _ in vals)

data = []
for f, v in zip(freq, vals):
    data.extend([v]*f)


def count_elements(seq) -> dict:
    """Tally elements from 'seq'"""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist


def ascii_histogram(seq)->None:
    """A horizontal frequency-table/hystogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print('{0:5d}{1}'.format(k, '+' * counted[k]))

ascii_histogram(data)
