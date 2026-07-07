# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        
        fast=head.next
        slow=head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            
        pointer=slow.next
        slow.next=None
        node=None
        
        while pointer:
            nxt=pointer.next
            pointer.next=node
            node=pointer
            pointer=nxt
            
            
        pointer=head
        while node:
            temp=node.next
            node.next=pointer.next
            pointer.next=node
            pointer=pointer.next.next
            node=temp