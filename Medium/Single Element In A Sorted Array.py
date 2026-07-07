class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(xor,nums)