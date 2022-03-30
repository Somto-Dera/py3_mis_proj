#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    # if (x1 - x2) % (v2 - v1) == 0 :
    
    assert 10000 >= v1 >= 1 and 10000 >= v2 >= 1
    assert 10000 >= x1 >= 0 and 10000 >= x2 >= 0

    while(x1 != x2):
        x1 += v1
        x2 += v2
        if x1 > 9999 or x2 > 9999:
            break

    if x1 - x2 == 0:
        return "YES"
    else:
        return "NO"


def kangaroos(x1, v1, x2, v2):
    if x2>x1 and v2>v1:
        return 'NO'
    elif (v2-v1) != 0 and (x2-x1)%(v1-v2)==0:
        return 'YES'
    else:
        return 'NO'

        
print(kangaroo(1928, 4306, 5763, 4301))