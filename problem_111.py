"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

https://leetcode.com/problems/minimum-depth-of-binary-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None or root.right is None:
            if root.left:
                return self.minDepth(root.left) + 1
            else:
                return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


"""
Runtime: 32 ms, faster than 98.89% of Python online submissions.
Memory Usage: 15.8 MB, less than 24.32% of Python online submissions.
Complexity: O(n), n is the depth of tree.
"""
