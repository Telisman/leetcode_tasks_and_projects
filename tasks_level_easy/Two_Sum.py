'''
Two Sum:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

# The given problem can be solved using a hash map to achieve a linear time complexity of O(n). Here's how you can implement the twoSum function:

class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  # Hash map to store number -> index mapping

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i  # Store the current number's index in the hash map

        # If no solution is found, return an empty list or raise an exception
        return []

# Create an instance of the Solution class
solution_instance = Solution()

# Define the input array and target value
nums = [2, 7, 11, 15]
target = 9

# Call the twoSum method on the instance and get the result
result = solution_instance.twoSum(nums, target)

print(result)  # Output: [0, 1]
