class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=b=0
        for i in nums:
            a,b=max(a,i),max(b,min(a,i))
        
        return (a-1)*(b-1)