"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

https://leetcode.com/problems/valid-perfect-square/

@author Mina HE
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for n in range(num):
            val = n**2
            if val == num:
                return True
            if val > num:
                return False
        return True


"""
Runtime: 40 ms, faster than 18.29% of Python online submissions.
Memory Usage: 13.7 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
