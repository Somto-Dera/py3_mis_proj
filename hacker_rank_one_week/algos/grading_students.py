#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grades = []

    for score in grades:
        if score < 38 or score % 5 == 0:
            new_grades.append(score)

        else:
            new_score = score
            while (new_score%5 != 0):
                    new_score += 1

            if new_score-score < 3:
                new_grades.append(new_score)

            else:
                new_grades.append(score)

    
    return new_grades



grds = [ 4, 73, 67, 38, 33 ]
print(gradingStudents(grds))