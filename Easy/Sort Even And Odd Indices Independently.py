class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        for i in [0, 1]:
            nums[i::2] = sorted(nums[i::2], reverse=i)
        return nums