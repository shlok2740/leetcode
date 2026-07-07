class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        last_index = 0
        for i,j in enumerate(nums):
            if i > last_index:
                break
                 
            if j!=0:
                last_index = max(last_index, j+i)
            
            if last_index >= len(nums) - 1:
                return True
        
        return False