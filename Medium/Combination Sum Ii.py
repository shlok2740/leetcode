class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(indx,nums,target,path,ret):
            if target <=0:
                if target==0:
                    ret.append(path)
                return
            for i in range(indx,len(nums)):
                
                if i>indx and nums[i]==nums[i-1]:
                    continue
                    
                dfs(i+1,nums,target-nums[i],path+[nums[i]],ret)
                
        ret=[]
        dfs(0,sorted(candidates),target,[],ret)
        return ret