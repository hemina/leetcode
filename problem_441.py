"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

https://leetcode.com/problems/arranging-coins/

@author Mina HE
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = i = 0
        while n >= s:
            i += 1
            s += i
        return i-1


"""
Runtime: 28 ms, faster than 81.01% of Python online submissions.
Memory Usage: 13.8 MB, less than 66.90% of Python online submissions.
Complexity: O(n)
"""
