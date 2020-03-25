"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters that may be separated by a single space.

https://leetcode.com/problems/word-pattern/

@author Mina HE
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_dict = dict()
        str_list = str.split()

        if len(pattern) != len(str_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in str_dict:
                if str_list[i] not in str_dict.values():
                    str_dict[pattern[i]] = str_list[i]
                else:
                    return False

        new_str = ' '.join([str_dict[char] for char in pattern])

        return new_str == str


"""
Runtime: 12 ms, faster than 90.04% of Python online submissions.
Memory Usage: 11.8 MB, less than 21.43% of Python online submissions.
Complexity: O(n)
"""
