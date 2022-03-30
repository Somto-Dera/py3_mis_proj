#!/bin/python3


#
# Complete the 'minimizeMemory' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processes
#  2. INTEGER m
#

def minimizeMemory(processes, m):
    # Write your code here
    sum_of_list = sum(processes)
    length_processes_list = len(processes)
    min_mem = sum_of_list

    for idx in range(0,length_processes_list - m):
        deleted = 0

        for item in range(idx, idx + m + 1):
            deleted += processes[item]

        if sum_of_list - deleted < min_mem:
            min_mem = sum_of_list - deleted
    
    return min_mem



processes = [4, 6, 10, 8, 2, 1]
m = 2
print(minimizeMemory(processes, m))
# 7