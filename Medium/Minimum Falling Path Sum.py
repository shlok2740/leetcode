class Solution:
    def minFallingPathSum(self, M: List[List[int]]) -> int:
        for i in range(1,len(M)):
            for j in range(len(M[0])):
                
                if j==0:
                    M[i][j]=min((M[i][j]+M[i-1][j]),(M[i][j]+M[i-1][j+1]))
                
                elif j==len(M[0])-1:
                    M[i][j]=min((M[i][j]+M[i-1][j]),(M[i][j]+M[i-1][j-1]))
                    
                else:
                    M[i][j]=min((M[i][j]+M[i-1][j]),(M[i][j]+M[i-1][j-1]),(M[i][j]+M[i-1][j+1]))
                    
        return min(M[len(M)-1])