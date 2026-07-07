class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        if rows==0:
            return -1
        
        cols=len(grid[0])
        
        fresh_count=0
        
        rotten=collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    rotten.append((r,c))
                    
                elif grid[r][c]==1:
                    fresh_count+=1
                    
        minutes_passed=0
        
        while rotten and fresh_count>0:
            
            minutes_passed+=1
            
            for _ in range(len(rotten)):
                x,y=rotten.popleft()
                
                for dx,dy in [(1,0),(0,1),(0,-1),(-1,0)]:
                    xx,yy=x+dx,y+dy
                    
                    if xx==rows or yy==cols or xx<0 or yy<0:
                        continue
                        
                    if grid[xx][yy]==2 or grid[xx][yy]==0:
                        continue
                        
                    fresh_count-=1
                    
                    grid[xx][yy]=2
                    
                    rotten.append((xx,yy))
                    
                    
        return minutes_passed if fresh_count==0 else -1