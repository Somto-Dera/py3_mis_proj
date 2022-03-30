#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    arr.sort()
    pos = 0
    neg = 0
    zeros = 0

    for item in arr:
        if item > 0:
            pos += 1

        elif item < 0:
            neg += 1

        else:
            zeros += 1

    pos = pos/len(arr)
    neg = neg/len(arr)
    zeros = zeros/len(arr)

    print(pos)
    print(neg)
    print(zeros)

    #return pos, neg, zeros




