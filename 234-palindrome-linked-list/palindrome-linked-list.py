# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        prev_add = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow: 
            nxt = slow.next 
            slow.next = prev_add 
            prev_add = slow 
            slow = nxt 
        while prev_add:
            if prev_add.val != head.val:
                return False
            prev_add = prev_add.next
            head = head.next
        return True
