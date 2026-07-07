class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        coins.sort()
        
        dp=[0]+[float('inf')]*(amount)
        
        for a in range(1,amount+1):
            for c in coins:
                if a>=c:
                    dp[a]=min(dp[a],dp[a-c]+1)
                else:
                    break
                    
        return dp[amount] if dp[amount] != math.inf else -1