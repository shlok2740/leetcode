class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        
        dpHigh=dpHighPrev=1
        dpLow=dpLowPrev=1
        
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                dpHigh=dpLowPrev+1
                dpLow=dpLowPrev
            elif nums[i]>nums[i-1]:
                dpLow=dpHighPrev+1
                dpHigh=dpHighPrev
            else:
                dpLow=dpLowPrev
                dpHigh=dpHighPrev
                
            dpHighPrev=dpHigh
            dpLowPrev=dpLow
            
        return max(dpLowPrev,dpHighPrev)