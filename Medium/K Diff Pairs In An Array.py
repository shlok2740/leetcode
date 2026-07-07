class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=0
        count=collections.Counter(nums)
        
        for i in count:
            if k>0 and i+k in count or k==0 and count[i]>1:
                ans+=1
                
        return ans