#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):

    # Write your code here

    # reverse_s = s[:: -1].split()
    # reverse_s = s[:: -1]

    # string = s.split()
    # string = s.split()

    length_of_string = len(s)

    if s == s[:: -1]:
        # return -1
        print(-1)

    # a[mid], a[length_of_string-1] = a[length_of_string-1], a[mid]

    median = int(length_of_string/2)

    st = 0
    ed = length_of_string - 1
    text = s
    while(st < ed/2):
        if s[st] != s[ed]:
            del text[ed]

        st += 1
        ed -= 1

    print(text)



s = "deifiged"
print(s[-1])
#print(palindromeIndex(s))


