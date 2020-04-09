"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.

https://leetcode.com/problems/cousins-in-binary-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build_cousins(self, root: TreeNode, depth: int):
        if root:
            if root.left or root.right:
                tmp_dict = self.cousins.get(depth, {})
                if root.left:
                    tmp_dict[root.left.val] = root.val
                if root.right:
                    tmp_dict[root.right.val] = root.val
                self.cousins[depth] = tmp_dict
            self.build_cousins(root.left, depth + 1)
            self.build_cousins(root.right, depth + 1)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.cousins = dict()
        self.build_cousins(root, 0)

        for depth, children_dict in self.cousins.items():
            parent_x = children_dict.get(x, None)
            parent_y = children_dict.get(y, None)
            if parent_x and parent_y and parent_x != parent_y:
                return True
        return False


"""
Runtime: 24 ms, faster than 96.34% of Python online submissions.
Memory Usage: 13.9 MB, less than 6.12% of Python online submissions.
Complexity: O(n)
"""
