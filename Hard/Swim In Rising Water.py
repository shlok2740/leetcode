class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visit=set()
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        minH=[[grid[0][0],0,0]]
        
        visit.add((0,0))
        
        while minH:
            t,r,c=heapq.heappop(minH)
            
            if (r,c)==(n-1,n-1):
                return t
            
            for i,j in directions:
                ri,cj=r+i,c+j
                
                if ri<0 or cj<0 or ri==n or cj==n or (ri,cj) in visit:
                    continue
                    
                visit.add((ri,cj))
                heapq.heappush(minH,[max(t,grid[ri][cj]),ri,cj])