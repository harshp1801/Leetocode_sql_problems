# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev_add = None
        curr = None
        while head:
            curr = head
            head = head.next
            curr.next = prev_add
            prev_add = curr
        return curr