class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.cache=set()
        def dfs(nums,target):
            if target<0:
                return False
            
            if target==0:
                return True
            
            if target in self.cache:
                return False
            
            self.cache.add(target)
            
            for indx,num in enumerate(nums):
                if dfs(nums[indx+1:],target-num) or dfs(nums[indx+1:],target):
                    return True
            return False
        
        if sum(nums)&1 !=0:
            return False
        sum_=sum(nums)
        return dfs(nums,sum_>>1)