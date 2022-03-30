#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    assert len(s) == 10

    x = s.split(":")
    h = int(x[0])

    if x[2][2:] == "AM" and h == 12:
        h = 0

    elif x[2][2:] == "PM" and h < 12:
        h += 12

    if h < 10:
        #print("0"+str(h)+":"+x[1]+":"+x[2][0:2]+x[2][2:])
        #print("\n")
        return ("0"+str(h)+":"+x[1]+":"+x[2][0:2])
    else:
        #print(str(h)+":"+x[1]+":"+x[2][0:2]+x[2][2:])
        #print("\n")
        return (str(h)+":"+x[1]+":"+x[2][0:2])

time_list = ["12:01:00PM", "01:01:00PM", "09:01:00AM", "12:01:00AM", "05:01:00PM"]
for tim in time_list:
    print(timeConversion(tim))
