"""
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.



Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
So you need to output 2.


Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0.
So you need to output 0.


Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

https://leetcode.com/problems/number-complement/

@author Mina HE
"""


class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        tmp = num
        while tmp > 0:
            i += 1
            tmp >>= 1
        return 2**i-1-num


"""
Runtime: 24 ms, faster than 89.09% of Python online submissions.
Memory Usage: 13.9 MB, less than 10.00% of Python online submissions.
Complexity: O(logn)
"""
