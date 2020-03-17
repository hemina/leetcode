"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

https://leetcode.com/problems/range-sum-query-immutable/

@author Mina HE
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_dict = {0: nums[0] if len(nums) > 0 else 0}
        for j in range(1, len(nums)):
            self.sum_dict[j] = self.sum_dict[j-1] + nums[j]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_dict[j] - self.sum_dict[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


"""
Runtime: 64 ms, faster than 88.97% of Python online submissions.
Memory Usage: 15.8 MB, less than 7.69% of Python online submissions.
Complexity: O(1)
"""
