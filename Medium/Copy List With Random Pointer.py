"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy_hashmap={None:None}
        
        cur=head
        while cur:
            copy=Node(cur.val)
            copy_hashmap[cur]=copy
            cur=cur.next
        
        cur=head
        while cur:
            copy=copy_hashmap[cur]
            copy.next=copy_hashmap[cur.next]
            copy.random=copy_hashmap[cur.random]
            cur=cur.next
            
        return copy_hashmap[head]