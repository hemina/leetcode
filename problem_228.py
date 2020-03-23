"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

https://leetcode.com/problems/summary-ranges/

@author Mina HE
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        def get_summary(base):
            if len(base) > 1:
                return str(base[0]) + '->' + str(base[-1])
            else:
                return str(base[0])

        base = [nums[0]]
        summary = []

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                base.append(nums[i])
            else:
                summary.append(get_summary(base))
                base = [nums[i]]

        summary.append(get_summary(base))
        return summary


"""
Runtime: 12 ms, faster than 89.22% of Python online submissions.
Memory Usage: 11.7 MB, less than 70.59% of Python online submissions.
Complexity: O(n)
"""
