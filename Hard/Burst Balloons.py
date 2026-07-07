class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]

        nums = [1] + nums + [1]
        n=len(nums)
        
        dp=[[0]*n for _ in range(n)]
        
        def burst(l,r):
            if dp[l][r] or r==l+1:
                return dp[l][r]
            
            coins=0
            for k in range(l+1,r):
                coins=max(coins,nums[l]*nums[k]*nums[r]+burst(l,k)+burst(k,r))
            dp[l][r]=coins
            return dp[l][r]
        
        return burst(0,n-1)