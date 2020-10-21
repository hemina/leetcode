"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

https://leetcode.com/problems/balanced-binary-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1 or abs(left-right)>1:
                return -1
            return 1+max(left, right)
        return height(root) != -1


"""
Runtime: 48 ms, faster than 85.86% of Python online submissions.
Memory Usage: 18.9 MB, less than 37.30% of Python online submissions.
"""