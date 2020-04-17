"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

https://leetcode.com/problems/valid-parenthesis-string/

@author Mina HE
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        # Simplify s to reduce complexity in further loop
        while s != s.replace("()", ""):
            s = s.replace("()", "")

        """
        The first loop, from left to right, is to check if there are supplementary ")" before "(".
        For example, a string like ")(*" won't be able to pass the first loop.
        """
        queue = []
        for i in range(len(s)):
            if s[i] in ["(", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False

        """
        The second loop, from right to left, is to check if there are supplementary "(" after ")".
        For example, a string like "*)(" won't be able to pass the second loop.
        """
        queue = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in [")", "*"]:
                queue.append(1)
            else:
                if queue:
                    queue.pop()
                else:
                    return False

        return True


"""
Runtime: 20 ms, faster than 98.16% of Python online submissions.
Memory Usage: 13.7 MB, less than 14.29% of Python online submissions.
Complexity: O(n)
"""
