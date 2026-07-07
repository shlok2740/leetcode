class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        r,c,arr=len(matrix),len(matrix[0]),[]
        
        for i in range(r):
            for j in range(c):
                if i and j:
                    matrix[i][j]^=matrix[i][j-1]^matrix[i-1][j]^matrix[i-1][j-1]
                elif i:
                    matrix[i][j]^=matrix[i-1][j]
                elif j:
                    matrix[i][j]^=matrix[i][j-1]
                
                arr.append(matrix[i][j])
        arr.sort()
        return arr[-k]