class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        b=nums[0]
        a=max(nums[1],nums[0])
        
        for i in range(2,len(nums)):
            c=max(a,b+nums[i])
            b=a
            a=c
            
        return a
            