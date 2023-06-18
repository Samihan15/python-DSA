#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    last = s[len(s)-2:]
    time = 0
    if last == 'PM':
        if s[:2] == '12':
            time = 12
        else:    
            time = 12 + int(s[:2])
    if last == 'AM':
        if int(s[:2]) < 12:
            time = s[:2]
            
        else:
            time = 12 - int(s[:2])
            if len(str(time)) == 1:
                time = str('0') + str(time)
    
    return str(time) + s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
