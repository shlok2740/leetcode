class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        if not rows:
            return 0
        
        cols=len(matrix[0])
        
        dp=[[0]*cols for _ in range(rows)]
        
        for i in range(rows):
            account=0
            
            for j in range(cols):
                if matrix[i][j]=="1":
                    account+=1
                else:
                    account=0
                    
                dp[i][j]=account
                
        result=0
        
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                
                bottom,right=dp[i][j],0
                times=i
                
                while times>-1 and dp[times][j]:
                    bottom=min(bottom,dp[times][j])
                    right+=1
                    
                    result=max(result,bottom*right)
                    times-=1
        
        return result