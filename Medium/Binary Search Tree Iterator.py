# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data=[-1]
        
        def inorder(root):
            if root:
                inorder(root.left)
                self.data.append(root.val)
                inorder(root.right)
        inorder(root)
        self.counter=0
        self.size=len(self.data)

    def next(self) -> int:
        self.counter+=1
        return self.data[self.counter]

    def hasNext(self) -> bool:
        return self.counter<self.size-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()