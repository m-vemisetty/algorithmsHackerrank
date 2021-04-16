#!/bin/python3
#https://www.hackerrank.com/challenges/plus-minus/problem
import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positiveVal =0
    negativeVal =0
    zeroVal =0
    for i in range(n):
        if arr[i]>0:
            positiveVal = positiveVal+1
        elif arr[i] == 0 :
            zeroVal = zeroVal+1
        else:
            negativeVal = negativeVal +1
    print("%f"%(positiveVal/n))
    print("%f"%(negativeVal/n))
    print("%f"%(zeroVal/n))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
