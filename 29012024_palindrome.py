# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 



 class Solution:
    def isPalindrome(self, x):

        str_x = str(x)

       
        return str_x == str_x[::-1]


sol = Solution()

x1 = 121
print(sol.isPalindrome(x1))  

x2 = -121
print(sol.isPalindrome(x2))  

x3 = 10
print(sol.isPalindrome(x3))  


