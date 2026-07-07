class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left,right,n=1,1,len(nums)
        
        ans=[1]*(n+1)
        
        for i in range(n):
            ans[i]*=left
            ans[n-i-1]*=right
            left*=nums[i]
            right*=nums[n-i-1]
            
            
        return ans[:-1]