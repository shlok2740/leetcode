class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        nums2=self.nums.copy()
        for i in range(len(self.nums)):
            indx=random.randrange(i,len(self.nums))
            nums2[i],nums2[indx]=nums2[indx],nums2[i]
        return nums2


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()