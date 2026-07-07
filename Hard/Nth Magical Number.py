class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def lcm(a,b):
            return a*(b//(gcd(a,b)))
        
        def pos(X,a,b):
            return (X//a) + (X//b) - (X//lcm(a,b))
        
        l=0
        r=10**18+1
        MOD=10**9+7
        
        
        while l<r:
            mid=(l+r)//2
            
            if pos(mid,a,b)<n:
                l=mid+1
            else:
                r=mid
                
        return l%MOD