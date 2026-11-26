# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode | None, nums: list[int]) -> int:
        cnt = 0
        while head:
            if head.val in nums:
                if head.next is not None:
                    if head.next.val in nums:
                        cnt+=1
            head = head.next
        return len(nums) - cnt
        