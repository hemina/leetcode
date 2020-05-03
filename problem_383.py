"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

https://leetcode.com/problems/ransom-note/

@author Mina HE
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_set = set(ransomNote)
        for char in ransom_set:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True


"""
Runtime: 24 ms, faster than 99.58% of Python online submissions.
Memory Usage: 14 MB, less than 25.00% of Python online submissions.
Complexity: O(n)
"""
