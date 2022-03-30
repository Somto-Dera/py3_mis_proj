#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    count_list = [0] * 100

    for item in arr:
        count_list[item] += 1

    print(count_list)
#    return count_list




arrayn = [1, 1, 3, 2, 1]
print (countingSort(arrayn))