"""
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2


Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

https://leetcode.com/problems/uncrossed-lines/

@author Mina HE
"""


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [-1] + A
        B = [0] + B
        len_A = len(A)
        len_B = len(B)
        table = [[0 for j in range(len_B)] for i in range(len_A)]
        for i in range(1, len_A):
            for j in range(1, len_B):
                if A[i] == B[j]:
                    table[i][j] = table[i-1][j-1]+1
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
        return table[-1][-1]


"""
Runtime: 208 ms, faster than 89.91% of Python online submissions.
Memory Usage: 14 MB, less than 46.81% of Python online submissions.
Complexity: O(m*n)
"""
