#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):

    arr.sort()
    min_arrayy = arr[:]
    max_arrayy = arr[:]

    del min_arrayy[-1]
    del max_arrayy[0]

    min = sum(min_arrayy)
    max = sum(max_arrayy)

    #print(min_arrayy)
    #print(max_arrayy)
    #print("max: ",max)
    #print("min: ",min)

    print(min,max)
    #return max,min


arr = [1, 3, 5 ,7, 9]

print(miniMaxSum(arr))
