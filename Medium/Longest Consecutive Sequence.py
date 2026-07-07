class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        res=1
        maxres=0
        
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                res+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                res=1
                
            maxres=max(res,maxres)
                
        return max(maxres,res) if nums else 0