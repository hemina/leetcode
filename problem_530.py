"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

https://leetcode.com/problems/minimum-absolute-difference-in-bst/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_values(values, root):
            if root is not None:
                values.append(root.val)
                values = get_values(values, root.left)
                values = get_values(values, root.right)
            return values

        values_list = get_values([], root)

        if len(values_list) != len(set(values_list)):
            return 0

        values_list.sort()
        minimum_diff = values_list[1] - values_list[0]

        for i in range(1, len(values_list)):
            diff = values_list[i] - values_list[i - 1]
            if diff < minimum_diff:
                minimum_diff = diff

        return minimum_diff


"""
Runtime: 44 ms, faster than 86.07% of Python online submissions.
Memory Usage: 16.1 MB, less than 25.00% of Python online submissions.
Complexity: O(nlogn)
"""
