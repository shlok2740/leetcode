class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        mid=n//2
        ans=0
        
        for i in range(n):
            ans+=mat[i][i]
            ans+=mat[n-i-1][i]
            
        if n%2:
            ans-=mat[mid][mid]
            
        return ans