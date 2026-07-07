# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        
        def solve(root):
            if not root:
                return
            cnt[root.val] += 1
            solve(root.left)
            solve(root.right)
        
        solve(root)
        
        mx = max(cnt.values())
        
        return [key for key, val in cnt.items() if val==mx]