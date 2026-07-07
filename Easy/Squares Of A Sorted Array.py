class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack=[]
        
        for i in nums:
            stack.append(i*i)
        
        stack.sort()
        
        return stack