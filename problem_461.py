"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

https://leetcode.com/problems/hamming-distance/

@author Mina HE
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


"""
Runtime: 20 ms, faster than 98.70% of Python online submissions.
Memory Usage: 13.9 MB, less than 27.50% of Python online submissions.
Complexity: O(n)
"""
