"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

https://leetcode.com/problems/minimum-path-sum/

@author Mina HE
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        nb_row = len(grid)
        nb_col = len(grid[0])

        for i in range(1, nb_col):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, nb_row):
            grid[j][0] += grid[j - 1][0]

        for i in range(1, nb_col):
            for j in range(1, nb_row):
                grid[j][i] += min(grid[j][i - 1], grid[j - 1][i])

        return grid[-1][-1]


"""
Runtime: 100 ms, faster than 73.41% of Python online submissions.
Memory Usage: 15.4 MB, less than 17.54% of Python online submissions.
Complexity: O(mn)
"""
