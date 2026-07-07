class Solution:
    def numTilings(self, n: int) -> int:
        MOD=(10**9)+7
        
        p3=-1
        p2=0
        p1=1
        
        for i in range(1,n+1):
            curr=(p1*2)+p3
            p3=p2
            p2=p1
            p1=curr
            
        return (curr%MOD)
            