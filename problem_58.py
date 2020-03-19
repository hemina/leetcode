"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

https://leetcode.com/problems/length-of-last-word/

@author Mina HE
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0


"""
Runtime: 12 ms, faster than 91.66% of Python online submissions.
Memory Usage: 11.8 MB, less than 60.71% of Python online submissions.
Complexity: O(n)
"""
