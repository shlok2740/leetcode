class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res,c=1,1
        
        for i in range(1,len(nums)):
            c=c+1 if nums[i-1]<nums[i] else 1
            res=max(res,c)
            
        return res