class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        level,res=-1,0
        
        for i in sorted(nums):
            if level < i:
                level=i
                
            else:
                level+=1
                res+=level-i
                
        return res