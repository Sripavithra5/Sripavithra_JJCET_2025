#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird
#Input Format

#A single line containing a positive integer, .

#Constraints

#Output Format

#Print Weird if the number is weird. Otherwise, print Not Weird.

#Sample Input 0

#3
#Sample Output 0

#Weird
#Explanation 0
#n=3
#n is odd and odd numbers are weird, so print Weird.

#Sample Input 1

#24
#Sample Output 1

#Not Weird
#Explanation 1
#n=24
#n>20 and n is even, so it is not weird.
#!/bin/python3

import math
import os
import random
import re
import sys
n=int(input().strip())
if n%2==0:
    if n>=2 and n<=5:
        print("not weird")
    elif n>=6 and n<=20:
        print("weird")
    else:
        print("not weird")
else:
    print("weird")