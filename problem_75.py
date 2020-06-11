"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

https://leetcode.com/problems/sort-colors/

@author Mina HE
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0  # indexing for 0
        j = 0  # indexing for 1
        n = len(nums)-1  # indexing for 2
        while j <= n:  # pass one by one
            if nums[j] < 1:  # if 0, swap current value with the following value of 0 indexing
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:  # if 2, swap current value with the preceding value of 2 indexing
                nums[j], nums[n] = nums[n], nums[j]
                n -= 1
            else:  # if 1, move on to the next value
                j += 1


"""
Runtime: 24 ms, faster than 97.71% of Python online submissions.
Memory Usage: 13.9 MB, less than 45.56% of Python online submissions.
Complexity: O(n)
"""
