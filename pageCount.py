#!/bin/python3
#https://www.hackerrank.com/challenges/drawing-book/problem
import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    front = p//2

    if n%2 == 1:
        back = (n-p)//2
    else:
        back = (n-p+1)//2

    return min(front,back)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
