#!/bin/python3
#https://www.hackerrank.com/challenges/sock-merchant/problem
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    d = {}

    for i in ar:
        d[i] = d.get(i,0) + 1

    for i in d.keys():
        count += d[i]//2

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
