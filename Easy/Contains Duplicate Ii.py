class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = {}
        for a,i in enumerate(nums):
            if i in s:
                if abs(s[i]-a)<=k:
                    return True
            s[i]=a
        return False