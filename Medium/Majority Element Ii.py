class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res={}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
                
        return [i for i in res if res[i]>n//3]