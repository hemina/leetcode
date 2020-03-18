"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6

https://leetcode.com/problems/guess-number-higher-or-lower/

@author Mina HE
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_val = n
        min_val = 1
        num = (n - 1)/2 + 1
        ans = guess(num)
        while ans != 0:
            if ans == -1:
                max_val = num - 1
            else:
                min_val = num + 1
            num = (max_val - min_val)/2 + min_val
            ans = guess(num)
        return num


"""
Runtime: 16 ms, faster than 72.18% of Python online submissions.
Memory Usage: 11.8 MB, less than 18.52% of Python online submissions.
Complexity: O(logn)
"""
