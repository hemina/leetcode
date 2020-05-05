"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

https://leetcode.com/problems/first-unique-character-in-a-string/

@author Mina HE
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
                if s.count(s[i]) == 1:
                    return i
        return -1


"""
Runtime: 60 ms, faster than 96.16% of Python online submissions.
Memory Usage: 14.1 MB, less than 6.52% of Python online submissions.
Complexity: O(nˆ2)
"""
