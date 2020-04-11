"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

https://leetcode.com/problems/surrounded-regions/

@author Mina HE
"""


# Time limit exceeded solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        if 'X' not in [s for row in board for s in row]:
            return
        nb_rows = len(board)
        nb_cols = len(board[0])
        x_positions = []
        o_positions = []
        o_borders = []
        move_row = [1, -1, 0, 0]
        move_col = [0, 0, 1, -1]
        visited = []

        for row in range(nb_rows):
            for col in range(nb_cols):
                if board[row][col] == 'O':
                    if row in [0, nb_rows - 1] or col in [0, nb_cols - 1]:
                        o_borders.append((row, col))
                    else:
                        o_positions.append((row, col))
                elif board[row][col] == 'X':
                    x_positions.append((row, col))

        # find all O connected with O border, put into new_o_borders
        new_o_borders = set(o_borders)
        while o_borders:
            (row, col) = o_borders.pop()
            for i in range(4):
                new_row = row + move_row[i]
                new_col = col + move_col[i]
                if (new_row, new_col) not in visited and (new_row, new_col) in o_positions:
                    visited.append((new_row, new_col))
                    o_borders.append((new_row, new_col))
                    new_o_borders.add((new_row, new_col))

        flipping = set(o_positions) - new_o_borders
        visited = []
        while x_positions:
            (row, col) = x_positions.pop()
            for i in range(4):
                new_row = row + move_row[i]
                new_col = col + move_col[i]
                if (new_row, new_col) in flipping and (new_row, new_col) not in visited:
                    visited.append((new_row, new_col))
                    board[new_row][new_col] = 'X'
                    x_positions.append((new_row, new_col))


# Efficient solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nb_row = len(board)
        nb_col = len(board[0]) if board else 0

        def helper(board, i: int, j: int) -> None:
            if 0 <= i < nb_row and 0 <= j < nb_col:
                if board[i][j] == 'O':
                    board[i][j] = 'D'
                    helper(board, i + 1, j)
                    helper(board, i - 1, j)
                    helper(board, i, j + 1)
                    helper(board, i, j - 1)

        # change left and right border O into D
        for row in range(nb_row):
            helper(board, row, 0)
            helper(board, row, nb_col - 1)

        # change up and down border O into D
        for col in range(nb_col):
            helper(board, 0, col)
            helper(board, nb_row - 1, col)

        for row in range(nb_row):
            for col in range(nb_col):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'D':
                    board[row][col] = 'O'


"""
Runtime: 132 ms, faster than 99.16% of Python online submissions.
Memory Usage: 15.5 MB, less than 13.33% of Python online submissions.
Complexity: O(n)
"""
