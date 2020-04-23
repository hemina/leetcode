"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0

https://leetcode.com/problems/bitwise-and-of-numbers-range/

@author Mina HE
"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        m <<= i
        return m


"""
Runtime: 56 ms, faster than 66.92% of Python online submissions.
Memory Usage: 13.8 MB, less than 100.00% of Python online submissions.
Complexity: O(logm)
"""
