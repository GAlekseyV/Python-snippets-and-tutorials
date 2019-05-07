# https://realpython.com/python-histograms/
# Building Up From the Base: Histogram Calculations in NumPy

import numpy as np
# 'numpy.random' uses its own PRNG.
np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)

hist, bin_edges = np.histogram(d)
first_edge, last_edge = d.min(), d.max()
n_equal_bins = 10
bin_edges = np.linspace(start=first_edge, stop=last_edge,
                        num=n_equal_bins + 1, endpoint=True)

bcounts = np.bincount(d)
hist, _ = np.histogram(d, range=(0, d.max()),bins=d.max() + 1)
