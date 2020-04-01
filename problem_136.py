"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

https://leetcode.com/problems/single-number/

@author Mina HE
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)


"""
Runtime: 80 ms, faster than 95.52% of Python online submissions.
Memory Usage: 15.4 MB, less than 6.56% of Python online submissions.
Complexity: O(n)
"""
