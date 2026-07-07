class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l=0
        r=sum(nums)
        
        res=[l+r]
        
        for i in nums:
            if i==0:
                l+=1   
            else:
                r-=1
                
            res.append(l+r)
            
        max_val=max(res)
        
        return [i for i,c in enumerate(res) if c==max_val]