class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}    
        def pick(r1, c1, r2, c2):
            k = r1, r2, c1, c2
            
            if k not in memo:
                
                if ((r1 < 0 or r2 < 0 or c1 < 0 or c2 < 0) or 
                    (grid[r1][c1] == -1 or grid[r2][c2] == -1)):
                    return float('-inf')
                
                if r1 == r2 == c1 == c2 == 0:
                    return grid[0][0]
                
                memo[k] = max(pick(r1-1, c1, r2-1, c2), pick(r1-1, c1, r2, c2-1),pick(r1, c1-1, r2-1, c2), pick(r1, c1-1, r2, c2-1)) + grid[r1][c1] + grid[r2][c2] - grid[r1][c1] * (r1==r2 and c1 == c2)
                    
            return memo[k]
        
        N = len(grid)
        res = pick(N-1, N-1, N-1, N-1)
        return 0 if res == float('-inf') else res