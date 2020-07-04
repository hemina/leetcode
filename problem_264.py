"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

https://leetcode.com/problems/ugly-number-ii/

@author Mina HE
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0,0,0
        while n > 1:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            min_u = min((u2, u3, u5))
            if min_u == u2:
                i2 += 1
            if min_u == u3:
                i3 += 1
            if min_u == u5:
                i5 += 1
            ugly.append(min_u)
            n -= 1
        return ugly[-1]


"""
Runtime: 152 ms, faster than 76.43% of Python online submissions.
Memory Usage: 13.8 MB, less than 87.93% of Python online submissions.
Complexity: O(n)
"""
