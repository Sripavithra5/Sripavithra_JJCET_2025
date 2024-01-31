# Animesh has  empty candy jars, numbered from  to , with infinite capacity. He performs  operations. Each operation is described by  integers, , , and . Here,  and  are indices of the jars, and  is the number of candies to be added inside each jar whose index lies between  and  (both inclusive). Can you tell the average number of candies after  operations?

# Example



# The array has  elements that all start at . In the first operation, add  to the first  elements. Now the array is . In the second operation, add  to the last  elements (3 - 5). Now the array is  and the average is 10. Sincd 10 is already an integer value, it does not need to be rounded.

# Function Description

# Complete the solve function in the editor below.

# solve has the following parameters:

# int n: the number of candy jars
# int operations[m][3]: a 2-dimensional array of operations
# Returns

# int: the floor of the average number of canidies in all jars
# Input Format

# The first line contains two integers,  and , separated by a single space.
 # lines follow. Each of them contains three integers, , , and , separated by# # spaces.

# Constraints





# STDIN       Function
-----       --------
# 5 3         n = 5, operations[] size = 3
# 1 2 100     operations = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
# 2 5 100
# 3 4 100
# Sample Output

# 160

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY operations
#

def solve(n, operations):

    output = 0

    for o in operations:

        output += o[2] * (o[1]-o[0]+1)

    return output//n



