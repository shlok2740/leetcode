class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i=0,arr=[]):
            
            if len(arr)==k:
                res.append(arr[:])
                return 
            
            for p in range(i,n):
                
                arr.append(nums[p])
                backtrack(p+1,arr)
                arr.pop()
                
        n=len(nums)
        res=[]
        
        for k in range(n+1):
            backtrack()
            
        return res