class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        
        q=collections.deque()
        q.append((0,0,0,k))
        
        visited=set()
        
        while q:
            x,y,count,k=q.popleft()
            
            if (x,y,k) in visited:
                continue
                
            visited.add((x,y,k))
            
            if (x,y) == (m-1,n-1):
                return count
            
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                xx,yy=x+dx,y+dy
                
                if not grid[x][y]:
                    
                    if 0<=xx<=m-1 and 0<=yy<=n-1:
                        q.append((xx,yy,count+1,k))
                        
                elif k:
                    
                    if 0<=xx<=m-1 and 0<=yy<=n-1:
                        q.append((xx,yy,count+1,k-1))
        return -1