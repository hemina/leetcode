"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

https://leetcode.com/problems/symmetric-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left)
        if root:
            return helper(root.left, root.right)
        return True


"""
Runtime: 28 ms, faster than 90.15% of Python online submissions.
Memory Usage: 14.1 MB, less than 5.17% of Python online submissions.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            current = stack.pop()
            if current[0] is None and current[1] is None:
                continue
            if current[0] is None or current[1] is None:
                return False
            if current[0].val == current[1].val:
                stack.append((current[0].left, current[1].right))
                stack.append((current[0].right, current[1].left))
            else:
                return False
        return True


"""
Runtime: 28 ms, faster than 90.15% of Python online submissions.
Memory Usage: 13.9 MB, less than 5.17% of Python online submissions.
"""
