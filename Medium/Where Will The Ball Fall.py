class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n=len(grid),len(grid[0])
        
        def dfs(r,c):
            if r==m:
                return c
            elif grid[r][c]==1 and c+1<n and grid[r][c+1]==1:
                return dfs(r+1,c+1)
            elif grid[r][c]==-1 and 0<=c-1 and grid[r][c-1]==-1:
                return dfs(r+1,c-1)
            else:
                return -1
            
        return [dfs(0,c) for c in range(n)] 