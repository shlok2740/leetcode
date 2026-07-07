class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        q=deque()
        moves=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        if grid[0][0]==0:
            q.append((1,(0,0)))
            grid[0][0]=1
            
        while q:
            steps,cell=q.popleft()
            x,y=cell[0],cell[1]
            if (x,y) == (m-1,n-1):
                return steps
            
            for dx,dy in moves:
                xx,yy=x+dx,y+dy
                
                if 0<=xx<m and 0<=yy<n and grid[xx][yy]==0:
                    q.append((steps+1,(xx,yy)))
                    grid[xx][yy]=1
                    
        return -1