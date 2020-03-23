"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

https://leetcode.com/problems/contains-duplicate-ii/

@author Mina HE
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if j - i <= k:
                        return True
        return False


"""
Runtime: 72 ms, faster than 90.80% of Python online submissions.
Memory Usage: 16 MB, less than 100.00% of Python online submissions.
Complexity: O(nˆ2)
"""
