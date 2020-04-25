"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

https://leetcode.com/problems/jump-game/

@author Mina HE
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        for i, num in enumerate(nums):
            if i > max_ind:
                return False
            max_ind = max(max_ind, i+num)
        return True


"""
Runtime: 88 ms, faster than 80.60% of Python online submissions.
Memory Usage: 15.8 MB, less than 7.14% of Python online submissions.
Complexity: O(n)
"""
