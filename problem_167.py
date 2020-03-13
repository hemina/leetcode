"""
Given an array of integers that is already sorted in ascending order, find two numbers such that
they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

@author Mina HE
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_set = set()
        for num in numbers:
            sub = target - num
            if sub in num_set:
                a = min(num, sub)
                b = max(num, sub)
                ind1 = numbers.index(a)
                numbers[ind1] = '#'
                ind2 = numbers.index(b)
                return [ind1+1, ind2+1]
            else:
                num_set.add(num)


"""
Runtime: 44ms, faster than 92.03 % of Python online submissions.
Memory Usage: 12MB, less than 60.00 % of Python online submissions.
Complexity: O(nˆ2)
"""
