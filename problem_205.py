"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

https://leetcode.com/problems/isomorphic-strings/

@author Mina HE
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = dict()
        for i in range(len(s)):
            if s[i] not in char_dict:
                if t[i] not in char_dict.values():
                    char_dict[s[i]] = t[i]
                else:
                    return False

        new_str = ''.join([char_dict[char] for char in s])
        return new_str == t


"""
Runtime: 20 ms, faster than 96.70% of Python online submissions.
Memory Usage: 14.6 MB, less than 36.84% of Python online submissions.
Complexity: O(n)
"""
