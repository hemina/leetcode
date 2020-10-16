"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        ind = len(nums) // 2
        root = TreeNode(nums[ind])
        root.left = self.sortedArrayToBST(nums[:ind])
        root.right = self.sortedArrayToBST(nums[ind + 1:])
        return root


"""
Runtime: 64 ms, faster than 97.28% of Python online submissions.
Memory Usage: 16.2 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
