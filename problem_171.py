"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".

https://leetcode.com/problems/excel-sheet-column-number/

@author Mina HE
"""


class Solution:
    def titleToNumber(self, s: str) -> int:
        alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        rev_s = list(s)[::-1]
        num = 0
        for i, char in enumerate(rev_s):
            num += alphabet.index(char)*(26**i)
        return num


"""
Runtime: 36 ms, faster than 43.21% of Python online submissions.
Memory Usage: 14.1 MB, less than 99.87% of Python online submissions.
Complexity: O(n)
"""
