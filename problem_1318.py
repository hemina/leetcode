"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ).
(bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.



Example 1:



Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0


Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9

https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

@author Mina HE
"""


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        sa = bin(a)[2:]
        sb = bin(b)[2:]
        s1 = bin(a | b)[2:]
        sc = bin(c)[2:]
        max_len = max(len(sc), len(s1))

        sa = (max_len - len(sa)) * '0' + sa
        sb = (max_len - len(sb)) * '0' + sb
        s1 = (max_len - len(s1)) * '0' + s1
        sc = (max_len - len(sc)) * '0' + sc

        counter = 0
        for i in range(max_len):
            if s1[i] != sc[i]:
                if sc[i] == '1':
                    counter += 1
                elif sc[i] == '0':
                    if sa[i] == sb[i]:
                        counter += 2
                    else:
                        counter += 1

        return counter


"""
Runtime: 20 ms, faster than 96.35% of Python online submissions.
Memory Usage: 14.1 MB, less than 100.00% of Python online submissions.
Complexity: O(logn)
"""
