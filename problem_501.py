"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

https://leetcode.com/problems/find-mode-in-binary-search-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        def get_value(values_dict, root):
            if root is not None:
                value = root.val
                if value not in values_dict:
                    values_dict[value] = 1
                else:
                    values_dict[value] += 1
                values_dict = get_value(values_dict, root.left)
                values_dict = get_value(values_dict, root.right)
            return values_dict

        values_dict = get_value(dict(), root)
        max_frequence = max(values_dict.values())
        return [node for node, count in values_dict.items() if count == max_frequence]


"""
Runtime: 44 ms, faster than 91.67% of Python online submissions.
Memory Usage: 19.8 MB, less than 55.56% of Python online submissions.
Complexity: O(n)
"""
