"""
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.

https://leetcode.com/problems/binary-number-with-alternating-bits/

@author Mina HE
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        return '00' not in s and '11' not in s


"""
Runtime: 24 ms, faster than 89.17% of Python online submissions.
Memory Usage: 13.8 MB, less than 20.00% of Python online submissions.
Complexity: O(1)
"""
