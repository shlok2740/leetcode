class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(n for n in nums if n<k)
        ans=0
        
        for i in count:
            ans+=min(count[i],count[k-i])
        
        return ans//2