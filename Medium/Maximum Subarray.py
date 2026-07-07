class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val,cur_val=-inf,0
        
        for i in nums:
            cur_val=max(cur_val+i,i)
            max_val=max(max_val,cur_val)
            
        return max_val