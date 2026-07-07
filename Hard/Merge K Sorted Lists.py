# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        h = []
        head = tail = ListNode(0)
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i, lists[i]))
            
        while h:
            node = heapq.heappop(h)
            node = node[2]
            tail.next = node
            tail = tail.next
            
            if node.next:
                i+=1
                heapq.heappush(h, (node.next.val, i, node.next))
                
                
        return head.next