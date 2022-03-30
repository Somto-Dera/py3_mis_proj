#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    lr = 0
    rl = 0
    i = 0
    j = int(arr[0]) - 1
    del arr[0]

    print()

    for item in arr:
        lr += arr[i][i]
        rl += arr[i][j]
        j -= 1
        i += 1

    print(lr, rl)
    return abs(lr-rl)



a = [3, [11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(a))