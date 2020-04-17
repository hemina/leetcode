"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

https://leetcode.com/problems/sqrtx/

@author Mina HE
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        min_val = 0
        max_val = x
        new_x = x // 2

        while new_x != min_val:
            if x < new_x ** 2:
                max_val = new_x
            elif x > new_x ** 2:
                min_val = new_x
            else:
                return new_x
            new_x = (min_val + max_val) // 2
        return new_x


"""
Runtime: 16 ms, faster than 92.83% of Python online submissions.
Memory Usage: 11.8 MB, less than 49.02% of Python online submissions.
Complexity: O(logn)
"""
