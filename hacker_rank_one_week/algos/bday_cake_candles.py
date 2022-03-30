#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    count = 0

    for item in candles:
        if item == candles[ -1 ]:
            count += 1


    return count





candle_sticks = [4, 4, 1, 3]
print(birthdayCakeCandles(candle_sticks))



