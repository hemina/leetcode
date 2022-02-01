"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

https://leetcode.com/problems/reverse-linked-list/

@author Mina HE
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            node = head
            head = head.next
            node.next = tail
            tail = node
        return tail


"""
Runtime: 24 ms, faster than 99.60% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 92.02% of Python3 online submissions for Reverse Linked List.
"""

class Solution:    
    def _recursive(self, node, tail):
        if not node:
            return tail
        n = node.next
        node.next = tail
        return self._recursive(n, node)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._recursive(head,None)

"""
Runtime: 40 ms, faster than 61.12% of Python3 online submissions for Reverse Linked List.
Memory Usage: 20.6 MB, less than 5.23% of Python3 online submissions for Reverse Linked List.  
"""      
