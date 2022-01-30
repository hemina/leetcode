
"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

https://leetcode.com/problems/pascals-triangle/
@author Mina HE
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1,numRows+1):
            row = [1]*i
            lastRow = triangle[-1] if triangle else []
            for j in range(1,len(lastRow)):
                row[j] = lastRow[j-1]+lastRow[j]
            triangle.append(row)
        return triangle

"""
Runtime: 27 ms, faster than 90.28% of Python3 online submissions.
Memory Usage: 13.9 MB, less than 97.20% of Python3 online submissions.
Complexity: O(n2)
"""        