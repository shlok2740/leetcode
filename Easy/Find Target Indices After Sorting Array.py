class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        equal=0
        small=0
        
        for x in nums:
            if x<target:
                small+=1
            if x==target:
                equal+=1
                
        return range(small,small+equal)