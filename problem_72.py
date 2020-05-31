"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

https://leetcode.com/problems/edit-distance/

@author Mina HE
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "*"+word1
        word2 = "*"+word2
        len_1 = len(word1)
        len_2 = len(word2)
        dist_matrix = [[0 for i in range(len_1)] for j in range(len_2)]
        for i in range(len_1):
            dist_matrix[0][i] = i
        for j in range(1, len_2):
            dist_matrix[j][0] = j
        for i in range(1, len_2):  # for row
            for j in range(1, len_1):  # for column
                if word1[j] == word2[i]:
                    dist_matrix[i][j] = dist_matrix[i-1][j-1]
                else:
                    dist_matrix[i][j] = min(
                        dist_matrix[i-1][j-1],  # replace word1[j] by word2[i]
                        dist_matrix[i][j-1],  # remove word1[j]
                        dist_matrix[i-1][j]  # insert word2[i]
                    ) + 1
        return dist_matrix[-1][-1]


"""
Runtime: 184 ms, faster than 70.79% of Python online submissions.
Memory Usage: 17.4 MB, less than 15.38% of Python online submissions.
Complexity: O(m*n)
"""
