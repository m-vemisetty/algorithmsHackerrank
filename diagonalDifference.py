#!/bin/python3
import math
import os
import random
import re
import sys
#https://www.hackerrank.com/challenges/diagonal-difference/problem
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    ldiag = rdiag = 0
    for i in range(n):
        ldiag = ldiag + arr[i][i]
        rdiag = rdiag + arr[i][n-1-i]
    return abs(ldiag-rdiag)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
