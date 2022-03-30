#!/bin/python3



#
# Complete the 'findEarliestMonth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY stockPrice as parameter.
#

def findEarliestMonth(stockPrice):
    # Write your code here
    month_list = []
    min_month = 0
    len_list = len(stockPrice)

    for idx in range(1, len_list):
        avg1 = 0
        avg2 = 0
        for item in range(0, idx):
            avg1 += stockPrice[item]
        avg1 //= (idx)

        for item in range(idx, len_list):
            avg2 += stockPrice[item]
        avg2 //= (len_list - idx)

        month_list.append(abs(avg1-avg2))

    temp = month_list[0]

    for idx in range(0, len(month_list)):
        if month_list[idx]<temp:
            temp = month_list[idx]
            min_month = idx + 1



    return min_month



stockPrices = [1, 3, 2, 3]
print(findEarliestMonth(stockPrices))
# 2