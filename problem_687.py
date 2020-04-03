"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.



Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2



Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2



Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

https://leetcode.com/problems/longest-univalue-path/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max = 0

    def helper(self, value: int, node: TreeNode) -> int:
        if node is None:
            return 0
        left_count = self.helper(node.val, node.left)  # if node.val != node.left.val, we have helper() equals to 0
        right_count = self.helper(node.val, node.right)
        self.max = max(self.max, left_count + right_count)

        if node.val == value:
            return 1 + max(left_count, right_count)
        return 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.helper(root.val, root)
        return self.max


"""
Runtime: 400 ms, faster than 86.67% of Python online submissions.
Memory Usage: 17.1 MB, less than 66.67% of Python online submissions.
"""
