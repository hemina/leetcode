"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

https://leetcode.com/problems/path-sum-iii/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        self.count = 0
        self.sum = sum

        def helper(root, val, sum_val):
            if root is None:
                return
            sum_val = [item + root.val for item in sum_val] + [root.val]
            self.count += sum_val.count(self.sum)
            helper(root.left, val, sum_val)
            helper(root.right, val, sum_val)

        helper(root, 0, [])
        return self.count


"""
Runtime: 204 ms, faster than 65.11% of Python online submissions.
Memory Usage: 30.5 MB, less than 9.09% of Python online submissions.
"""
