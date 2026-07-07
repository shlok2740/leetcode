class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0]*(n+2)
        nums[1]=1
        
        for i in range(n+1):
            if (2*i)+1<=n:
                nums[2*i]=nums[i]
                nums[(2*i)+1]=nums[i]+nums[i+1]
                
        return max(nums[:n+1])