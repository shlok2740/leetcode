class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxsum=nums[0]
        cursum=nums[0]
        
        for i in range(len(nums)-1):
            
            if nums[i+1]>nums[i]:
                cursum+=nums[i+1]
            else:
                cursum=nums[i+1]
            maxsum=max(maxsum,cursum,nums[i+1])
            
        return max(maxsum,cursum)