# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head

    def getRandom(self) -> int:
        curr=self.head
        ans=self.head
        n=1
        while curr.next:
            n+=1
            curr=curr.next
            if random.randint(1,n)==(n-1):
                ans=curr
        return ans.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()