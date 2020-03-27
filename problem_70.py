"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

https://leetcode.com/problems/climbing-stairs/

@author Mina HE
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = 0
        for i in range(int(n/2) + 1):  # i is the possible number of 2-step climb, from 0 to n/2 max
            numerator = n - 2 * i + 1
            denominator = i
            count = div = 1
            while numerator <= n - i:
                count = count * numerator
                numerator += 1
                div = div * denominator
                denominator -= 1
            s += count / div
        return s


"""
Runtime:  8 ms, faster than 97.44% of Python online submissions.
Memory Usage: 12.7 MB, less than 6.25% of Python online submissions.
Complexity: O(n^2)
"""
