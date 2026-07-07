class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(b-a for a,b in zip(nums,nums[k-1:]))