class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid,i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or grid[i][j] == 0:
                return 0
            
            grid[i][j]=0
            return 1 + dfs(grid,i+1,j) + dfs(grid,i-1,j) + dfs(grid,i,j+1) + dfs(grid,i,j-1)
        
        ans,m,n=0,len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans=max(ans,dfs(grid,i,j))
                
        return ans