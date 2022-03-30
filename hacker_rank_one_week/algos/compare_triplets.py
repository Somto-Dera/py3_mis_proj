#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    al_score = 0
    bob_score = 0

    assert len(a) == len(b)

    for idx in range(0,len(a)):
        if a[idx] > b[idx]:
            al_score += 1

        elif a[idx] < b[idx]:
            bob_score += 1

        else:
            pass

    return [al_score,bob_score]


a = [5, 6, 7]
b = [3, 6, 10]
print(compareTriplets(a,b))


