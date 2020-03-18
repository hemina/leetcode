"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

https://leetcode.com/problems/first-bad-version/

@author Mina HE
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        min_ind = 1
        max_ind = n
        while (max_ind - min_ind > 1):
            ind = (max_ind - min_ind)/2+min_ind
            ans = isBadVersion(ind)
            if ans:
                max_ind = ind
            else:
                min_ind = ind
        return max_ind


"""
Runtime: 12 ms, faster than 88.07% of Python online submissions.
Memory Usage: 11.8 MB, less than 52.78% of Python online submissions.
Complexity: O(logn)
"""
