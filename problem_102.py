"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

https://leetcode.com/problems/binary-tree-level-order-traversal/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_nodes(self, root: TreeNode, level: int) -> None:
        if root:
            tmp = self.level_dict.get(level, [])
            tmp.append(root.val)
            self.level_dict[level] = tmp
            self.get_nodes(root.left, level + 1)
            self.get_nodes(root.right, level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.level_dict = dict()
        self.get_nodes(root, 0)
        return [nodes for nodes in self.level_dict.values()]


"""
Runtime: 28 ms, faster than 91.69% of Python online submissions.
Memory Usage: 14.2 MB, less than 6.45% of Python online submissions.
Complexity: O(n)
"""
