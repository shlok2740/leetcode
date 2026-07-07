class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start=end=None
        visit=set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    start=(r,c)
                elif grid[r][c]==2:
                    end=(r,c)
                    visit.add(end)
                elif grid[r][c]==0:
                    visit.add((r,c))
        
        def backtrack(x,y,visit):
            if (x, y) == end:
                return len(visit) == 0
            result = 0
            
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (i,j) in visit:
                    visit.remove((i,j))
                    result += backtrack(i,j,visit)
                    visit.add((i,j))
            
            return result
        
        return backtrack(start[0],start[1],visit)