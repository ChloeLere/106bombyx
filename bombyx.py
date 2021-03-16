#!/usr/bin/env python3

import sys
import math
from calc import growth
from calc import generations

def display_h(argv):
    if argv[1][0] == '-' and argv[1][1] == 'h':
        print("USAGE")
        print("     ./106bombyx n [k | i0 i1]\n")
        print("DESCRIPTION")
        print("    n       number of first generation individuals")
        print("    k       growth rate from 1 to 4")
        print("    i0      initial generation (included)")
        print("    i1      final generation (included)")
        return 1
    return 0

def error(argv):
    if len(argv) < 3 or len(argv) > 4:
        sys.stderr.write("Error: not enough/too many argument\n")
        return 84
    for i in range(1, len(argv)):
        for x in range(0, len(argv[i])):
            if ((argv[i][x] < '0' or argv[i][x] > '9') and argv[i][x] != '.'):
                sys.stderr.write("SyntaxError: invalid syntax\n")
                return 84
    if int(argv[1]) == 0:
        sys.stderr.write("SyntaxError: invalid syntax\n")
        return 84
    return 0
    

def main(argv):
    if len(argv) == 1:
        sys.stderr.write("Error: not enough argument\n")
        return 84
    if display_h(argv) == 1:
        return 0
    if error(argv) == 84:
        return 84
    if len(argv) == 3:
        if float(argv[2]) < 1 or float(argv[2]) > 4:
            sys.stderr.write("SyntaxError: invalid syntax\n")
            return 84
        growth(argv)
    else:
        generations(argv)
    return 0