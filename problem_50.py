"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

https://leetcode.com/problems/powx-n/

@author Mina HE
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            tmp = helper(x, n // 2)
            if n % 2 == 0:
                return tmp * tmp
            if n % 2 == 1:
                return x * tmp * tmp

        if n >= 0:
            return helper(x, n)

        return 1 / helper(x, -n)


"""
Runtime: 16 ms, faster than 99.43% of Python online submissions.
Memory Usage: 14 MB, less than 6.90% of Python online submissions.
Complexity: O(logn)
"""
