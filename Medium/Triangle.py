class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        
        for r in range(1,n):
            for c in range(r+1):
                
                if c==0:
                    triangle[r][c]+=triangle[r-1][c]
                elif c==r:
                    triangle[r][c]+=triangle[r-1][c-1]
                else:
                    triangle[r][c]+=min(triangle[r-1][c],triangle[r-1][c-1])
                    
        ans=math.inf
        
        for c in range(n):
            ans=min(ans,triangle[n-1][c])
        return ans