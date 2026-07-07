class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp=collections.Counter([0])
        
        for num in nums:
            for key,val in list(dp.items()):
                dp[key|num]+=val
                
        return dp[max(dp)]