"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

@author Mina HE
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def helper(root: TreeNode, depth: int, ans: List[List[int]]):
            if root:
                if len(ans) < depth + 1:  # ensure the length of answer equal to the depth of tree
                    ans.insert(0, [])
                ans[-(depth + 1)].append(root.val)
                helper(root.left, depth + 1, ans)
                helper(root.right, depth + 1, ans)
            return ans

        return helper(root, 0, [])


"""
Runtime: 28 ms, faster than 92.31% of Python online submissions.
Memory Usage: 14.5 MB, less than 7.41% of Python online submissions.
Complexity: O(n)
"""
