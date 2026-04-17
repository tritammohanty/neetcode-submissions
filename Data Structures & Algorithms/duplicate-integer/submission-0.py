""" 
Q: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

E1: 
Input: nums = [1, 2, 3, 3]
Output: true

E2:
Input: nums = [1, 2, 3, 4]
Output: false
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
