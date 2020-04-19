"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

https://leetcode.com/problems/search-in-rotated-sorted-array/

@author Mina HE
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        first = 0
        last = len(nums) - 1

        while first <= last:
            ind = (last - first) // 2 + first
            if target == nums[ind]:
                return ind

            if nums[ind] == nums[first]:  # when there are at most 2 numbers in the list
                if target == nums[last]:
                    return last
                return -1

            if nums[ind] > nums[first]:  # monotone increasing from first to ind
                if nums[first] <= target < nums[ind]:
                    last = ind
                else:
                    first = ind
            else:  # when nums[ind]<nums[first] monotone increasing from ind to last
                if nums[ind] < target <= nums[last]:
                    first = ind
                else:
                    last = ind
        return -1


"""
Runtime: 32 ms, faster than 96.87% of Python online submissions.
Memory Usage: 14.1 MB, less than 6.29% of Python online submissions.
Complexity: O(mn)
"""
