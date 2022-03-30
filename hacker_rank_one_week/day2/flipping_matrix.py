#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    col =[]
    row = []
    sample = len(matrix)
    x = 0

    while x<sample:
        col.append(matrix[2][x])
        x += 1
    x = 0
    col.reverse()
    
    while x<sample:
        row.append(matrix[x][0])
        x += 1
    x = 0
    row.reverse()

    
    for i in range(0,sample):
        matrix[2][i] = col[i]
        matrix[i][0] = row[i]

    return matrix






matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
print(len(matrix))
print(flippingMatrix(matrix))
