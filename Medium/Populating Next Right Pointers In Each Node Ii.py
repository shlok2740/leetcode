"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q=deque()
        if root:
            q.append(root)
        while q:
            size=len(q)
            for i in range(size):
                l=q.popleft()
                if i !=size-1:
                    l.next=q[0]
                if l.left:
                    q.append(l.left)
                if l.right:
                    q.append(l.right)
        return root