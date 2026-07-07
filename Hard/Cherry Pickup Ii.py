class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        
        @lru_cache(None)
        def helper(row,col1,col2):
            
            cherries=grid[row][col1]
            if col1 != col2:
                cherries += grid[row][col2]
                
                
            if row == rows-1:
                return cherries
            
            temp=0
            
            for m1 in (col1-1,col1,col1+1):
                for m2 in (col2-1,col2,col2+1):
                    
                    if 0<=m1<cols and 0<=m2<cols:
                        temp=max(temp,helper(row+1,m1,m2))
                        
            return temp + cherries
        
        return helper(0,0,cols-1)