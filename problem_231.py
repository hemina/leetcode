"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

https://leetcode.com/problems/power-of-two/

@author Mina HE
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        val = 1
        while val < n:
            i += 1
            val = 2 ** i
        if val == n:
            return True
        return False


"""
Runtime: 28 ms, faster than 82.51% of Python online submissions.
Memory Usage: 13.8 MB, less than 46.21% of Python online submissions.
Complexity: O(logn)
"""
