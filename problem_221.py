"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

https://leetcode.com/problems/maximal-square/

@author Mina HE
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nb_row = len(matrix)
        nb_col = len(matrix[0])
        d = dict()

        for row in range(nb_row):
            d[(row, 0)] = int(matrix[row][0])

        for col in range(nb_col):
            d[(0, col)] = int(matrix[0][col])

        side = max(d.values())
        for row in range(1, nb_row):
            for col in range(1, nb_col):
                d[(row, col)] = int(matrix[row][col]) and 1 + min(
                    d[(row - 1, col - 1)], d[(row, col - 1)], d[(row - 1, col)])
                side = max(side, d[(row, col)])
        return side ** 2


"""
Runtime: 216 ms, faster than 45.27% of Python online submissions.
Memory Usage: 19 MB, less than 9.09% of Python online submissions.
Complexity: O(n)
"""
