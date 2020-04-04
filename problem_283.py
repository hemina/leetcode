"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

https://leetcode.com/problems/move-zeroes/

@author Mina HE
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        counter = 0
        while i < len(nums)-counter:
            if nums[i] == 0:
                counter += 1
                nums.pop(i)
                nums.append(0)
                i -= 1
            i += 1


"""
Runtime: 44 ms, faster than 90.65% of Python online submissions.
Memory Usage: 15.1 MB, less than 5.97% of Python online submissions.
Complexity: O(n)
"""
