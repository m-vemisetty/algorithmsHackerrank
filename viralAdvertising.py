#!/bin/python3
#https://www.hackerrank.com/challenges/strange-advertising/problem
import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    totalLikes  = 0
    shared = 5
    for i in range(n):
        like = shared//2
        totalLikes += like
        shared = like*3
    return totalLikes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
