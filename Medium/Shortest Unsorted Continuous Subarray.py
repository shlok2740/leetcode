class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2=sorted(nums)
        if nums==nums2:
            return 0 
        
        l=0
        r=len(nums)-1
        
        while l<r:
            if nums[l]==nums2[l]:
                l+=1
            elif nums[r]==nums2[r]:
                r-=1
            else:
                return r-l+1
            
        