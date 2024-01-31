# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format
#  Returns

# string: the time in  hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

# Constraints

# All input times are valid
# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45





def timeConversion(s):
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    am_pm = s[-2:]
    if am_pm == 'AM' and hours == 12:
        hours = 0
    elif am_pm == 'PM' and hours != 12:
        hours += 12
    result = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    return result
s = '07:05:45PM'
result = timeConversion(s)
print(result)

if _name_ == '_main_':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
def timeConversion(s):
  

    if s[-2:] == "AM" and s[:2] == "12": 

        return "00" + s[2:-2] 

    elif s[-2:] == "AM": 

        return s[:-2]

    elif s[-2:] == "PM" and s[:2] == "12": 

        return s[:-2] 

    else:

       ans = int(s[:2]) + 12

       return str(str(ans) + s[2:8]) 

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()