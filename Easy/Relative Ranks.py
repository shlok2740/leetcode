class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_sorted = sorted(nums, reverse = True)
        
        s = {score : index for index, score in enumerate(nums_sorted)}
        
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]
        
        result = [medals[s[n]] for n in nums]
        
        return result