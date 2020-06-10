"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

https://leetcode.com/problems/search-insert-position/

@author Mina HE
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,num in enumerate(nums):
            if num >= target:
                return i
        return i+1


"""
Runtime: 44 ms, faster than 92.39% of Python online submissions.
Memory Usage: 14.5 MB, less than 72.47% of Python online submissions.
Complexity: O(n)
"""
