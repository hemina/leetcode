"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

https://leetcode.com/problems/island-perimeter/

@author Mina HE
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nb_row = len(grid)
        nb_col = len(grid[0])
        perimeter = 0

        for row in range(nb_row):
            for col in range(nb_col):
                if grid[row][col] == 1:
                    perimeter += 4
                    if col > 0 and grid[row][col - 1] == 1:
                        perimeter -= 2
                    if row > 0 and grid[row - 1][col] == 1:
                        perimeter -= 2
        return perimeter


"""
Runtime: 424 ms, faster than 95.90% of Python online submissions.
Memory Usage: 12.2 MB, less than 11.76% of Python online submissions.
Complexity: O(m*n)
"""
