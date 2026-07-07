class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            left = target - nums[i]

            if left in seen:
                return [seen[left], i]

            seen[value] = i

