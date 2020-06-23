"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

https://leetcode.com/problems/count-complete-tree-nodes/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


"""
Runtime: 88 ms, faster than 57.81% of Python online submissions.
Memory Usage: 21.1 MB, less than 75.46% of Python online submissions.
Complexity: O(n)
"""


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(node):
            if not node:
                return -1
            return 1+height(node.left)
        h = height(root)
        if h < 0:
            return 0
        right_h = height(root.right)
        if right_h == h - 1:  # while root.left is full, we only need to count the nodes in root.right
            return (1 << h) + self.countNodes(root.right)
        return (1 << (h-1)) + self.countNodes(root.left)
        # while root.right is not at the height of root.left, we know the h-1 level is complete,
        # we only need to count the nodes in root.left


"""
Runtime: 72 ms, faster than 96.02% of Python online submissions.
Memory Usage: 21.2 MB, less than 74.32% of Python online submissions.
Complexity: O(n)
"""
