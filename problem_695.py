"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

https://leetcode.com/problems/max-area-of-island/

@author Mina HE
"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nb_row = len(grid)
        nb_col = len(grid[0])

        self.visited = set()

        max_land = 0

        delta_row = [0, 0, 1, -1]
        delta_col = [1, -1, 0, 0]

        def get_land(row, col, land):
            if (row, col) not in self.visited:
                self.visited.add((row, col))
                if grid[row][col] == 1:
                    land += 1
                    for i in range(4):
                        new_row = row + delta_row[i]
                        new_col = col + delta_col[i]
                        if new_row >= 0 and new_row < nb_row and new_col >= 0 and new_col < nb_col:
                            land = get_land(new_row, new_col, land)
            return land

        for row in range(nb_row):
            for col in range(nb_col):
                if (row, col) not in self.visited:
                    if grid[row][col] == 1:
                        max_land = max(get_land(row, col, 0), max_land)

        return max_land


"""
Runtime: 148 ms, faster than 26.51% of Python online submissions.
Memory Usage: 16.7 MB, less than 5.88% of Python online submissions.
Complexity: O(m*n)
"""
