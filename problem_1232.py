"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

https://leetcode.com/problems/check-if-it-is-a-straight-line/

@author Mina HE
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]

        x1 = coordinates[1][0]
        y1 = coordinates[1][1]

        if x0 == x1:
            return False
        slope = (y1 - y0) / (x1 - x0)

        for [x, y] in coordinates[2:]:
            delta_y = y - y0
            delta_x = x - x0
            if slope * delta_x != delta_y:
                return False
        return True


"""
Runtime: 56 ms, faster than 92.34% of Python online submissions.
Memory Usage: 14 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
