# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        
        def traverse(left_cursor: int, right_cursor: int):
            if left_cursor > right_cursor:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = traverse(index + 1, right_cursor)
            root.left = traverse(left_cursor,index -1)
            return root
        
        return traverse(0, len(inorder) -1)