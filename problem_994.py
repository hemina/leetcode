"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

https://leetcode.com/problems/rotting-oranges/

@author Mina HE
"""

import copy


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nb_rows = len(grid)
        nb_cols = len(grid[0])
        move_x = [0, 0, 1, -1]
        move_y = [1, -1, 0, 0]
        time = 0
        visited = set()
        new_grid = copy.deepcopy(grid)

        grid_set = set([num for l in grid for num in l])
        if 1 in grid_set and 2 not in grid_set:
            return -1
        if 1 not in grid_set and 2 in grid_set:
            return 0

        while 1 in grid_set and 2 in grid_set:
            time += 1
            for i in range(nb_rows):
                for j in range(nb_cols):
                    if grid[i][j] == 2 and [i, j] not in visited:
                        visited.add([i, j])
                        for k in range(4):
                            new_x = i + move_x[k]
                            new_y = j + move_y[k]
                            if new_x >= 0 and new_x < nb_rows and new_y >= 0 and new_y < nb_cols:
                                if grid[new_x][new_y] == 1:
                                    new_grid[new_x][new_y] = 2
            if new_grid == grid:
                return -1
            grid_set = set([num for l in new_grid for num in l])
            grid = copy.deepcopy(new_grid)
        return time


"""
Runtime: 80 ms, faster than 7.93% of Python online submissions.
Memory Usage: 13.8 MB, less than 16.67% of Python online submissions.
Complexity: O(n^2)
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nb_rows = len(grid)
        nb_cols = len(grid[0])
        move_x = [0, 0, 1, -1]
        move_y = [1, -1, 0, 0]
        time = 0
        queue = []
        new_queue = []

        grid_set = set([num for l in grid for num in l])
        if 1 in grid_set and 2 not in grid_set:
            return -1
        if 1 not in grid_set and 2 in grid_set:
            return 0

        for i in range(nb_rows):
            for j in range(nb_cols):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:
            (i, j) = queue.pop(0)
            for k in range(4):
                new_x = i + move_x[k]
                new_y = j + move_y[k]
                if new_x >= 0 and new_x < nb_rows and new_y >= 0 and new_y < nb_cols:
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        new_queue.append((new_x, new_y))
            if not queue:
                if new_queue:
                    time += 1
                    queue = new_queue
                    new_queue = []

        grid_set = set([num for l in grid for num in l])
        if 1 in grid_set:
            return -1
        return time


"""
Runtime: 44 ms, faster than 94.46% of Python online submissions.
Memory Usage: 13.8 MB, less than 16.67% of Python online submissions.
Complexity: O(n)
"""
