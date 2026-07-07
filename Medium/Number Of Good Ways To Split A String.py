class Solution:
    def numSplits(self, s: str) -> int:
        left=collections.Counter()
        right=collections.Counter(s)
        res=0
        
        for i in s:
            left[i]+=1
            right[i]-=1
            
            if right[i]==0:
                del right[i]
                
            
            if len(left)==len(right):
                res+=1
                
        return res