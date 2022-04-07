#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alp = tuple('abcdefghijklmnopqrstuvwxyz')
    alpUpper = tuple(''.join(alp).upper())
    arr = list(s) # [m,i,d,d,l,e,-,O,u,t,z]
    res = []
    for item in arr:
        if item in alp:
            res.append(alp[(alp.index(item)+k)%len(alp)])
        elif item in alpUpper:
            res.append(alpUpper[(alpUpper.index(item)+k)%len(alpUpper)])
        else:
            res.append(item)
            
    return ''.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
