# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        trav = root
        res = []
        stack = []
        while stack or trav:
            while trav:
                stack.append(trav)
                trav = trav.left
            u = stack.pop()
            res.append(u.val)
            trav = u.right
        return res