class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        q = deque()
        dummy = ListNode(-1,head)

        pre = dummy
        p = head
        while p != None:
            while p != None and len(q) < k:
                q.append(p)
                p = p.next
            if len(q) == k:
                while len(q) > 0:
                    pre.next = q.pop();
                    pre = pre.next
                pre.next = p
        return dummy.next