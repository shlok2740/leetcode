class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points=[0]*10001
        
        prev,curr=0,0
        
        for num in nums:
            points[num]+=num
            
        for point in points:
            prev,curr=curr,max(prev+point,curr)
            
        return curr