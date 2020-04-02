"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

https://leetcode.com/problems/happy-number/

@author Mina HE
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def get_num(n):
            s = 0

            while n >= 10:
                s += (n % 10) ** 2
                n = n // 10

            s += n ** 2
            if s <= 10:
                return s

            return get_num(s)

        return True if get_num(n) in [1, 7, 10] else False


"""
Runtime: 12 ms, faster than 97.76% of Python online submissions.
Memory Usage: 11.7 MB, less than 50.00% of Python online submissions.
"""
