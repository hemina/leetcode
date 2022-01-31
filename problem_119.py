
"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

https://leetcode.com/problems/pascals-triangle-ii/
@author Mina HE
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        for i in range(0, rowIndex+1):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] = lastRow[j-1]+lastRow[j]
            lastRow = row
        return lastRow

"""
Runtime: 36 ms, faster than 48.31% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.9 MB, less than 98.97% of Python3 online submissions for Pascal's Triangle II.
Complexity: O(n2)
"""        