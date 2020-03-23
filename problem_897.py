"""
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9


Constraints:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.

https://leetcode.com/problems/increasing-order-search-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.all_nodes = []

        def find_all_nodes(root):
            if root:
                self.all_nodes.append(root.val)
                find_all_nodes(root.left)
                find_all_nodes(root.right)

        find_all_nodes(root)
        self.all_nodes.sort()

        tree = TreeNode(self.all_nodes.pop())
        while len(self.all_nodes) > 0:
            t = TreeNode(self.all_nodes.pop())
            t.left = None
            t.right = tree
            tree = t

        return tree


"""
Runtime: 16 ms, faster than 97.98% of Python online submissions.
Memory Usage: 11.9 MB, less than 66.67% of Python online submissions.
Complexity: O(nlogn)
"""
