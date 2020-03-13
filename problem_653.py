"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that
their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

@author Mina HE
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nodes = [root]
        num_set = set()
        for node in nodes:
            if k-node.val in num_set:
                return True
            num_set.add(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return False


"""
Runtime: 64 ms, faster than 88.18% of Python online submissions.
Memory Usage: 16.4 MB, less than 23.53% of Python online submissions.
Complexity: O(nˆ2)
"""
