"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

https://leetcode.com/problems/binary-tree-paths/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, path):
            if not root:
                return []
            path += str(root.val)
            if not root.left and not root.right:
                return [path]
            path += "->"
            return dfs(root.left, path) + dfs(root.right, path)
        return dfs(root, "")


"""
Runtime: 28 ms, faster than 90.13% of Python online submissions.
Memory Usage: 14.1 MB, less than 100.00% of Python online submissions.
"""
