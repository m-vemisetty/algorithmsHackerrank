#!/bin/python3
#https://www.hackerrank.com/challenges/the-birthday-bar/problem
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    total = sum(s[:m])

    if total == d:
        count += 1

    for i in range(m, len(s)):
        total += s[i]
        total -= s[i-m]
        if total == d:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
