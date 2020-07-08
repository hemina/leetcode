"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

https://leetcode.com/problems/3sum/

@author Mina HE
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = set()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            d = dict()
            for j in range(i+1, n):
                if nums[j] not in d:
                    d[-nums[i]-nums[j]] = 1
                else:
                    res.add((nums[i], nums[j], -nums[i]-nums[j]))
        return map(list, res)


"""
Runtime: 1328 ms, faster than 35.19% of Python online submissions.
Memory Usage: 17.3 MB, less than 47.53% of Python online submissions.
"""
