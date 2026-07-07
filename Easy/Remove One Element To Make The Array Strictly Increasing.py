class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def inc(arr):
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    return False
            return True
        
        for i in range(len(nums)):
            if inc(nums[:i] + nums[i + 1:]):
                return True

        return False