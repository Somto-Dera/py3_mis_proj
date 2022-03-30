#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here

    k %= 26

    encoded_text = ""
    idx = 0
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    cypher_alpha = alphabets[ k : ] + alphabets[ : k ]
    upper_cypher_alpha = cypher_alpha.upper()
    # print(alphabets)
    # print(cypher_alpha)
    # print(upper_cypher_alpha)
    for letter in s:

        
        
        if letter in cypher_alpha or letter in upper_cypher_alpha:
            if letter.islower() == True:
                idx = alphabets.index(letter)
                encoded_text += cypher_alpha[idx]

            else:
                temp = letter.lower()
                idx = alphabets.index(temp)
                encoded_text += upper_cypher_alpha[idx]

        else:
            encoded_text += letter



    return encoded_text



text = "www.abc.xy"
rot_fac = 2
print(caesarCipher(text,rot_fac))