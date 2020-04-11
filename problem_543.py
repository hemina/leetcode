"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

https://leetcode.com/problems/diameter-of-binary-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def path_length(self, root: TreeNode, length: int):
        if root:
            left_path = self.path_length(root.left, 0)
            right_path = self.path_length(root.right, 0)
            path = left_path + right_path
            if path > self.diameter:
                self.diameter = path
            return max(left_path, right_path) + length + 1
        return length

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.path_length(root, 0)
        return self.diameter


"""
Runtime: 36 ms, faster than 96.53% of Python online submissions.
Memory Usage: 15.6 MB, less than 65.52% of Python online submissions.
Complexity: O(n)
"""
