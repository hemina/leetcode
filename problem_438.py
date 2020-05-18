"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only
and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

https://leetcode.com/problems/find-all-anagrams-in-a-string/

@author Mina HE
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        S = 0
        P = 0
        ans = []
        if len_p > len_s:
            return []

        for i in range(len_p):
            S += hash(s[i])
            P += hash(p[i])

        if S == P:
            ans.append(0)

        for i in range(len_p, len_s):
            S += hash(s[i]) - hash(s[i - len_p])
            if S == P:
                ans.append(i - len_p + 1)
        return ans


"""
Runtime: 76 ms, faster than 98.68% of Python online submissions.
Memory Usage: 14.9 MB, less than 8.70% of Python online submissions.
Complexity: O(n)
"""
