"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

https://leetcode.com/problems/contiguous-array/

@author Mina HE
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_dict = {0: -1}
        s = 0
        maxlen = 0
        for i, value in enumerate(nums):
            if value == 1:
                s += 1
            elif value == 0:
                s -= 1
            if s in sum_dict:
                maxlen = max(maxlen, i-sum_dict[s])
            else:
                sum_dict[s] = i
        return maxlen


"""
Runtime: 904 ms, faster than 83.31% of Python online submissions.
Memory Usage: 18.4 MB, less than 16.67% of Python online submissions.
Complexity: O(n^2)
"""
