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


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_count = len(nums)//2
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
                if nums.count(num) > min_count:
                    return num


"""
Runtime: 160 ms, faster than 98.42% of Python online submissions.
Memory Usage: 15 MB, less than 7.14% of Python online submissions.
Complexity: O(n^2)
"""
