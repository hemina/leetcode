"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

https://leetcode.com/problems/backspace-string-compare/

@author Mina HE
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def get_str(S: str) -> str:
            str_s = ''
            for i in range(len(S)):
                if S[i] != '#':
                    str_s += S[i]
                else:
                    str_s = str_s[:-1]
            return str_s
        return get_str(S) == get_str(T)


"""
Runtime: 20 ms, faster than 98.37% of Python online submissions.
Memory Usage: 13.7 MB, less than 8.00% of Python online submissions.
Complexity: O(n)
"""
