"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

https://leetcode.com/problems/binary-tree-maximum-path-sum/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node) -> int:
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        self.maxsum = max(self.maxsum, left + right + node.val)
        return max(left + node.val, right + node.val, 0)

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = root.val
        self.helper(root)
        return self.maxsum


"""
Runtime: 76 ms, faster than 99.08% of Python online submissions.
Memory Usage: 20.1 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
