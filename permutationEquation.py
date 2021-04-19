#!/bin/python3
#https://www.hackerrank.com/challenges/permutation-equation/problem
import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    res = []
    n = len(p)
    for i in range(1, n+1):
        res.append(p.index(p.index(i)+1)+1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
