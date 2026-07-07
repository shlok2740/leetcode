class Solution:
    def knightProbability(self, N: int, K: int, row: int, column: int) -> float:
        dp=[[[0]*N for _ in range(N)] for _ in range(K+1)]
        dp[0][row][column]=1
        moves=[(-2,1),(2,-1),(2,1),(-2,-1),(1,2),(-1,-2),(1,-2),(-1,2)]
        
        for k in range(K+1):
            for i in range(N):
                for j in range(N):
                    for di,dj in moves:
                        x,y=i+di,j+dj
                        if x<0 or x>N-1 or y<0 or y>N-1:
                            continue
                        dp[k][i][j]+=dp[k-1][x][y]*0.125
                        
        return sum(i for row in dp[-1] for i in row)