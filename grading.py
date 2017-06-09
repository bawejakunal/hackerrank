#!/bin/python3

"""
https://www.hackerrank.com/challenges/grading
"""

import sys

def round_grade(grade):
    if grade >= 38 and (grade % 5) > 2:
        return grade + 5 - (grade % 5)
    else:
        return grade

def solve(grades):
    result = grades.copy()
    for i in range(len(result)):
        result[i] = round_grade(result[i])
    return result

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
