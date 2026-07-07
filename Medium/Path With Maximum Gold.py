class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        res=0
        visited=set()
        
        def dfs(r,c,res):
            if (r<0 or c<0 or r>m-1 or c>n-1 or (r,c) in visited or grid[r][c]==0):
                return res
            
            res+=grid[r][c]
            visited.add((r,c))
            
            gold=0
            for i,j in [[0,1],[1,0],[0,-1],[-1,0]]:
                gold=max(gold,dfs(r+i,c+j,res))
                
            visited.remove((r,c))
            return gold
        
        return max(dfs(i,j,0) for i in range(m) for j in range(n))