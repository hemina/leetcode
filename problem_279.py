"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

https://leetcode.com/problems/perfect-squares/

@author Mina HE
"""


class Solution:
    def numSquares(self, n: int) -> int:
        root = int(sqrt(n))
        sqr = root ** 2
        if sqr == n:
            return 1
        for i in range(root + 1):
            tmp = n - i ** 2
            if int(sqrt(tmp)) ** 2 == tmp:
                return 2
        while n % 4 == 0:
            n = n >> 2
        if n % 8 == 7:
            return 4
        return 3


"""
Runtime: 24 ms, faster than 99.89% of Python online submissions.
Memory Usage: 13.8 MB, less than 83.41% of Python online submissions.
Complexity: O(nˆ(1/2))
"""
