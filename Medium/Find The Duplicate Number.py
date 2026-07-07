class Solution:
    def findDuplicate(self, nums: List[float]) -> float:
        n=len(nums)-1
        nums.sort()
        seen=[0]*(n+1)
        for i in nums:
            if seen[i]:
                return i
            seen[i]=1
                    