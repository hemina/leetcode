"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it.
If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples.
You will not have access the binary matrix directly.



Example 1:



Input: mat = [[0,0],[1,1]]
Output: 0
Example 2:



Input: mat = [[0,0],[0,1]]
Output: 1
Example 3:



Input: mat = [[0,0],[0,0]]
Output: -1
Example 4:



Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:

1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.

https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

@author Mina HE
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [nb_row, nb_col] = binaryMatrix.dimensions()

        # if "1" in the first column
        for row in range(nb_row):
            if binaryMatrix.get(row, 0) == 1:
                return 0

        # if no "1" in the last column
        counter = 0
        for row in range(nb_row):
            if binaryMatrix.get(row, nb_col - 1) == 1:
                counter += 1
        if counter == 0:
            return -1

        ind = -1
        first = 0
        last = nb_col
        col = nb_col // 2
        while col < last:
            counter = 0
            for row in range(nb_row):
                if binaryMatrix.get(row, col) == 1:
                    counter += 1
                    ind = last = col
                    col = max(col // 2, first)
                    break  # we find at least one "1" in the "last" column
            if counter == 0:  # we can't find any "1" in this column
                first = max(first, col + 1)
                col = (last - first) // 2 + first
        return ind


"""
Runtime: 112 ms
Memory Usage: 14 MB
Complexity: O(nlogm)
"""
