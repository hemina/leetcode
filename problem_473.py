"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

https://leetcode.com/problems/matchsticks-to-square

@author Mina HE
"""


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False

        side = sum(nums) / 4.
        if side != int(side):
            return False

        nums.sort(reverse=True)
        if nums[0] > side:
            return False

        square_sides = [0, 0, 0, 0]

        def dfs(index):
            if index == n:
                return square_sides[0] == square_sides[1] == square_sides[2] == side
            for i in range(4):
                if square_sides[i] + nums[index] <= side:
                    square_sides[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    square_sides[i] -= nums[index]
            return False

        return dfs(0)


"""
Runtime: 1792 ms, faster than 13.09% of Python online submissions.
Memory Usage: 11.9 MB, less than 100.00% of Python online submissions.
Complexity: O(4^n)
"""
##################################################################################


class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 4:
            return False

        s = sum(nums)
        if s % 4 != 0:
            return False

        side = s // 4
        visited = [False] * n
        nums.sort(reverse=True)

        if nums[0] > side:
            return False

        def dfs(nums, val, i, side, visited, n):
            if val == side:
                return True, visited
            for k in range(i + 1, n):
                if not visited[k] and nums[k] + val <= side:
                    visited[k] = True
                    flag, visited = dfs(nums, nums[k] + val, i, side, visited, n)
                    if flag:
                        return flag, visited
                    visited[k] = False
            return False, visited

        for i, num in enumerate(nums):
            if not visited[i]:
                visited[i] = True
                flag, visited = dfs(nums, num, i, side, visited, n)
                if not flag:
                    return False
        return flag


"""
Runtime: 36 ms, faster than 89.29% of Python online submissions.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions.
Complexity: O(n^2)
"""



