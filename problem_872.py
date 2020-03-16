"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.

https://leetcode.com/problems/leaf-similar-trees/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.get_leaves(root1) == self.get_leaves(root2)

    def get_leaves(self, root):
        if root is None:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.get_leaves(root.left) + self.get_leaves(root.right)


"""
Runtime: 20 ms, faster than 70.18% of Python online submissions.
Memory Usage: 11.9 MB, less than 50.00% of Python online submissions.
Complexity: O(logn)
"""
