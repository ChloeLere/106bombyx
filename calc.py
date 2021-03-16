#!/usr/bin/env python3

import sys
import math
import numpy as np

def growth(argv):
    k = float(argv[2])
    xi = float(argv[1])
    xn = float(0)
    i = 1

    print(i, "%.2f" % xi)
    for i in range(1, 100):
        i += 1
        xn = k * xi * ((1000 - xi) / (1000))
        xi = xn
        print(i, "%.2f" % xn)

def generations(argv):
    k = 1.00
    xi = float(argv[1])

    for k in np.arange(1, 4, 0.01):
        for n in range(1, int(argv[3]) + 1):
            if n >= float(argv[2]):
                print("%.2f" % k, "%.2f" % xi)
            xn = (k * xi * ((1000 - xi))) / 1000
            xi = xn
        xi = float(argv[1])