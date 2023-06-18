#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    length = len(arr)
    for i in arr:
        if i < 0:
            negative += 1
        if i > 0:
            positive += 1
        if i == 0:
            zero += 1
            
    print(f'{positive/length:.6f}\n{negative/length:.6f}\n{zero/length:.6f}')
    
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
