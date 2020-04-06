"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

https://leetcode.com/problems/group-anagrams/

@author Mina HE
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return groups.values()


"""
Runtime: 96 ms, faster than 87.51% of Python online submissions.
Memory Usage: 17 MB, less than 37.74% of Python online submissions.
Complexity: O(n)
"""
