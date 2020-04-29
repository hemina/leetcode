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
        max_side = 0
        for row in range(nb_row):
            matrix[row][0] = int(matrix[row][0])
            max_side = max(max_side, matrix[row][0])
        for col in range(nb_col):
            matrix[0][col] = int(matrix[0][col])
            max_side = max(max_side, matrix[0][col])
        for row in range(1, nb_row):
            for col in range(1, nb_col):
                matrix[row][col] = int(matrix[row][col]) and min(
                    matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1])+1
                max_side = max(matrix[row][col], max_side)
        return max_side**2


"""
Runtime: 200 ms, faster than 74.45% of Python online submissions.
Memory Usage: 14.6 MB, less than 9.09% of Python online submissions.
Complexity: O(n)
"""
