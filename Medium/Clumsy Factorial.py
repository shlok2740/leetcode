class Solution:
    def clumsy(self, n: int) -> int:
        return [0,1,2,6,7][n] if n<5 else n+[1,2,2,-1][n%4]