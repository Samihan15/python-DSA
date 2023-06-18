#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    mini = min(arr)
    maxi = max(arr)
    
    small = 0
    large = 0
    
    for i in arr:
        
        if i < maxi:
            small += i
        if i > mini:
            large += i
        if (i == mini) and (i == maxi) and (arr.count(mini) == len(arr)):
            small += i
            large += i
        
    if (mini == maxi) and arr.count(mini) == len(arr):
        small = small - mini
        large = large - mini 
        
    print(small,large)
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
