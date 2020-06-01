"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so f*** off.

https://leetcode.com/problems/invert-binary-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


"""
Runtime: 24 ms, faster than 92.73% of Python online submissions.
Memory Usage: 13.7 MB, less than 5.41% of Python online submissions.
Complexity: O(n)
"""
