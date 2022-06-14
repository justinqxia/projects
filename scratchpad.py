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
    # Write your code here
    result=s[0:8]
    if("A"==s[8:9]):
        if("12"==s[0:2]):
            result.replace("12","00",1)
    else:
        if("12"!=s[0:2]):
            hour=int(s[0:2])
            hour=hour+12
            result.replace(s[0:2],str(hour),1)
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
