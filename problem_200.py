"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

https://leetcode.com/problems/number-of-islands/

@author Mina HE
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        if not grid:
            return 0

        def helper(grid, x, y, nb_row, nb_col):
            if 0 <= x < nb_row and 0 <= y < nb_col:
                if grid[x][y] == "1":
                    grid[x][y] = "0"
                    helper(grid, x + 1, y, nb_row, nb_col)
                    helper(grid, x - 1, y, nb_row, nb_col)
                    helper(grid, x, y + 1, nb_row, nb_col)
                    helper(grid, x, y - 1, nb_row, nb_col)

        nb_row = len(grid)
        nb_col = len(grid[0])

        for i in range(nb_row):
            for j in range(nb_col):
                if grid[i][j] == "1":
                    count += 1
                    helper(grid, i, j, nb_row, nb_col)

        return count


"""
Runtime: 120 ms, faster than 99.48 % of Python online submissions.
Memory Usage: 14.9 MB, less than 9.40% of Python online submissions.
Complexity: O(mn)
"""
