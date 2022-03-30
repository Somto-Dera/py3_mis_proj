#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    arr = a[:]
    array_counter = {}
    lonely = 0

    for item in arr:
        if item not in array_counter:
            array_counter[item] = 1

        else:
            array_counter[item] += 1

    #print (array_counter)

    for item in array_counter:

        if array_counter[item] == 1:
            lonely = item

    return lonely






        

        
        


a = [1, 2, 3, 4, 3, 2, 1]
print(lonelyinteger(a))