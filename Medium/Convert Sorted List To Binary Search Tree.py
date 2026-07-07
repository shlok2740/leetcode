# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return self.dfs(stack)

    def dfs(self, stack):
        if stack:
            m = (len(stack) - 1) // 2
            root = TreeNode(stack[m])
            root.left = self.dfs(stack[:m])
            root.right = self.dfs(stack[m + 1:])
            return root