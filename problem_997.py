"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b]
representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.



Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N

https://leetcode.com/problems/find-the-town-judge/

@author Mina HE
"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_dict = dict()
        for [k, v] in trust:
            tmp_set = trust_dict.get(k, set())
            tmp_set.add(v)
            trust_dict[k] = tmp_set

        judge_set = set(range(1, N + 1)) - set(trust_dict.keys())  # people who trust nobody

        if len(judge_set) != 1:  # when there are more than one person who trust nobody, or everyone trust someone
            return -1

        for v in trust_dict.values():
            judge_set = judge_set & v  # people trusted by everyone

        if not judge_set:
            return -1

        return list(judge_set)[0]


"""
Runtime: 800 ms, faster than 50.86% of Python online submissions.
Memory Usage: 18.3 MB, less than 10.00% of Python online submissions.
Complexity: O(m+n)
"""
