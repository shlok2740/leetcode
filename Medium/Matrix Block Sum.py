import numpy as np
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        mat2=np.array(mat)
        m=len(mat)
        n=len(mat[0])
        
        for i in range(m):
            for j in range(n):
                
                least_i=max(0,i-k)
                most_i=min(m,i+k)
                
                least_j=max(0,j-k)
                most_j=min(m,j+k)
                
                mat[i][j] = np.sum(mat2[least_i : most_i+1 , least_j : most_j+1])
                
        
        
        return mat