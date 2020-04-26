"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string
with some characters(can be none) deleted without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.

https://leetcode.com/problems/longest-common-subsequence/

@author Mina HE
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1 = set(text1)
        set2 = set(text2)
        if not set1 & set2:
            return 0

        text1 = "1" + text1
        text2 = "2" + text2

        len1 = len(text1)
        len2 = len(text2)

        count_matrix = [[0 for i in range(len1)] for j in range(len2)]

        for i in range(1, len1):
            count_matrix[0][i] = 1 if text1[i] == text2[0] else 0

        for j in range(1, len2):
            count_matrix[j][0] = 1 if text1[0] == text2[j] else 0

        for i in range(1, len1):
            for j in range(1, len2):
                count_matrix[j][i] = max(count_matrix[j][i - 1], count_matrix[j - 1][i])
                if text1[i] == text2[j]:
                    count_matrix[j][i] = max(count_matrix[j - 1][i - 1] + 1, count_matrix[j][i])

        return count_matrix[-1][-1]


"""
Runtime: 436 ms, faster than 67.17% of Python online submissions.
Memory Usage: 22.4 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
