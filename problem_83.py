"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

@author Mina HE
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current = dummy_head
        while current.next.next is not None:
            if current.next.val == current.next.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next


"""
Runtime: 32 ms, faster than 54.46% of Python online submissions.
Memory Usage: 11.9 MB, less than 46.43% of Python online submissions.
Complexity: O(n)
"""
