"""
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())        #The .strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters. 
if n%2 ==1 or n>=6 and n<=20:       # Combining both the statements which tell us to print weird 
    print("Weird")
elif n>=2 and n<=5 or n>=20:        # Combining both the statements which tell us to print not weird
    print("Not Weird")
