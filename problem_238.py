"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array
(including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)

https://leetcode.com/problems/product-of-array-except-self

@author Mina HE
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = []
        for num in nums:
            ans.append(product)
            product = product * num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * product
            product = product * nums[i]

        return ans


"""
Runtime: 120 ms, faster than 85.97% of Python online submissions.
Memory Usage: 20.5 MB, less than 78.00% of Python online submissions.
Complexity: O(n)
"""
