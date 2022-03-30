#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    print (arr)
    print(len(arr)/2)
    return arr[int((len(arr)/2)-0.5)]



arr = [5, 3, 1, 2, 4]
print(findMedian(arr))