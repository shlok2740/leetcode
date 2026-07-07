class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]
        
        def solve(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]:
                return 0
            
            if i==m-1 and j==n-1:
                return 1
            
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j]=solve(i+1,j)+solve(i,j+1)
            return dp[i][j]
        
        return solve(0,0)