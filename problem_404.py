"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

https://leetcode.com/problems/sum-of-left-leaves/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def is_leave(root):
            return root.left is None and root.right is None

        sum_value = 0
        if root is not None:
            if root.left:
                if is_leave(root.left):
                    sum_value += root.left.val
                else:
                    sum_value += self.sumOfLeftLeaves(root.left)
            sum_value += self.sumOfLeftLeaves(root.right)
        return sum_value


"""
Runtime: 12 ms, faster than 98.38% of Python online submissions.
Memory Usage: 12.5 MB, less than 66.67% of Python online submissions.
Complexity: O(n)
"""
