# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]



class Solution:
    def twoSum(self, nums, target):
        # Create a hashmap to store the indices of elements
        num_indices = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the hashmap
            if complement in num_indices:
                # If found, return the indices of the two numbers
                return [num_indices[complement], i]

            # Otherwise, add the current number and its index to the hashmap
            num_indices[num] = i

        # If no solution is found, return an empty list (this should not happen based on the problem statement)
        return []


nums1 = [2, 7, 11, 15]
target1 = 9
sol = Solution()
print(sol.twoSum(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(sol.twoSum(nums2, target2))  

nums3 = [3, 3]
target3 = 6
print(sol.twoSum(nums3, target3))  

 