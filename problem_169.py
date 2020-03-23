"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

https://leetcode.com/problems/majority-element/

@author Mina HE
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter_dict = dict()

        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 0
            counter_dict[num] += 1
            if counter_dict[num] > len(nums) / 2:
                return num


"""
Runtime: 156 ms, faster than 57.85% of Python online submissions.
Memory Usage: 13.3 MB, less than 92.68% of Python online submissions.
Complexity: O(n)
"""
