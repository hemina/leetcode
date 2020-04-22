"""
Given an array of integers and an integer k,
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

https://leetcode.com/problems/subarray-sum-equals-k/

@author Mina HE
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        counter = 0
        sum_dict = {0: 1}

        for num in nums:
            s += num
            counter += sum_dict.get(s - k, 0)
            sum_dict[s] = sum_dict.get(s, 0) + 1

        return counter


"""
Runtime: 100 ms, faster than 99.15% of Python online submissions.
Memory Usage: 16.1 MB, less than 20.00% of Python online submissions.
Complexity: O(n)
"""
