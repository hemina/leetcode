"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

https://leetcode.com/problems/valid-anagram/

@author Mina HE
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or set(s) != set(t):
            return False

        alphabets = dict()
        for char in s:
            if char in alphabets:
                alphabets[char] += 1
            else:
                alphabets[char] = 1

        for char in t:
            alphabets[char] -= 1

        for v in alphabets.values():
            if v != 0:
                return False

        return True


"""
Runtime: 40 ms, faster than 82.66% of Python online submissions.
Memory Usage: 14.1 MB, less than 9.38% of Python online submissions.
Complexity: O(n^2)
"""
