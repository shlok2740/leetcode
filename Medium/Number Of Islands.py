class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]=="0":
                return
            
            visit.add((r,c))
            for (x,y) in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r+x,c+y)
                
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    islands+=1
                    
        return islands