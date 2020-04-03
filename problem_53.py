"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

https://leetcode.com/problems/maximum-subarray/

@author Mina HE
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = ans = nums[0]

        for i in range(1, len(nums)):
            s = max(0, s) + nums[i]
            ans = ans if ans > s else s

        return ans


"""
Runtime: 60 ms, faster than 94.34% of Python online submissions.
Memory Usage: 14.5 MB, less than 5.69% of Python online submissions.
Complexity: O(n)
"""
