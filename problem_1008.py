"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first,
then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.

https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def build_right(tree, value):
            if not tree.right:
                tree.right = TreeNode(value)
            elif tree.right.val < value:
                build_right(tree.right, value)
            else:
                build_left(tree.right, value)

        def build_left(tree, value):
            if not tree.left:
                tree.left = TreeNode(value)
            elif tree.left.val < value:
                build_right(tree.left, value)
            else:
                build_left(tree.left, value)

        tree = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                build_right(tree, preorder[i])
            else:
                build_left(tree, preorder[i])
        return tree


"""
Runtime: 32 ms, faster than 86.34% of Python online submissions.
Memory Usage: 13.7 MB, less than 6.67% of Python online submissions.
Complexity: O(nlogn)
"""


# Another similar solution with only one recursive function


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def helper(tree, value):
            if not tree:
                tree = TreeNode(value)
            elif tree.val > value:
                tree.left = helper(tree.left, value)
            else:
                tree.right = helper(tree.right, value)
            return tree

        tree = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                tree.right = helper(tree.right, preorder[i])
            else:
                tree.left = helper(tree.left, preorder[i])
        return tree


"""
Runtime: 32 ms, faster than 86.34% of Python online submissions.
Memory Usage: 13.7 MB, less than 6.67% of Python online submissions.
Complexity: O(nlogn)
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def helper(value, node):
            if value < node.val:
                if not node.left:
                    node.left = TreeNode(value)
                else:
                    helper(value, node.left)
            else:
                if not node.right:
                    node.right = TreeNode(value)
                else:
                    helper(value, node.right)
            return node

        root = TreeNode(preorder[0])
        for value in preorder[1:]:
            root = helper(value, root)
        return root


"""
Runtime: 28 ms, faster than 96.84% of Python online submissions.
Memory Usage: 13.9 MB, less than 6.67% of Python online submissions.
Complexity: O(nlogn)
"""
