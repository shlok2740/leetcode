class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        
        def dfs(i,path,ret,target,candidates):
            if target<0:
                return
            if target==0:
                ret.append(path)
                return
            for i in range(len(candidates)):
                dfs(i,path+[candidates[i]],ret,target-candidates[i],candidates[i:])
                
        dfs(0,[],ret,target,candidates)
        return ret