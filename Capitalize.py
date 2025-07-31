#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    listed_name = list(s)
    
    for i in range(len(listed_name)):
        if i == 0:
            listed_name[i] = listed_name[i].upper()
        elif listed_name[i] == " ":
            listed_name[i + 1] = listed_name[i + 1].upper()
    
    result = "".join(listed_name)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
