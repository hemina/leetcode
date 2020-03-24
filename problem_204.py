"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

https://leetcode.com/problems/count-primes/

@author Mina HE
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        prime_ind = [0, 0] + [1] * (n - 2)
        max_i = int(n ** 0.5) + 1

        for i in range(2, max_i):
            if prime_ind[i] == 1:
                max_j = n // i + 1
                for j in range(2, max_j):
                    if i * j < n:
                        prime_ind[i * j] = 0

        return sum(prime_ind)


"""
Runtime: 740 ms, faster than 52.94% of Python online submissions.
Memory Usage: 50.7 MB, less than 40.74% of Python online submissions.
"""
