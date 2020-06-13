"""
Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

https://leetcode.com/problems/largest-divisible-subset/

@author Mina HE
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        subsets=[[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[i]) < len(subsets[j]) + 1:
                    # if nums[i] have the same number of factors as nums[j]
                    subsets[i] = subsets[i] + [nums[j]]
        return max(subsets, key=len)


"""
Runtime: 424 ms, faster than 72.33% of Python online submissions.
Memory Usage: 13.8 MB, less than 92.88% of Python online submissions.
Complexity: O(n^2)
"""
