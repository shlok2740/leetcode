class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums,path):
            if not nums:
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                new=nums[:i]+nums[i+1:]
                path.append(nums[i])
                backtrack(new,path)
                path.pop()
                
        res=[]
        backtrack(nums,[])
        return res