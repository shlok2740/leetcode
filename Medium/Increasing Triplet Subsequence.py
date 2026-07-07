class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp=[(float("inf"))]*2
        
        for num in nums:
            if num<dp[0]:
                dp[0]=num
            elif dp[0]<num<dp[1]:
                dp[1]=num
            elif num>dp[1]:
                return True
            
        return False