class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for i in range(n-1):
            l, r = i+1, n-1 # starting the search
            while l < r:
                temp_sum = nums[l] + nums[r] + nums[i]
                # if we are above the target, reduce the bigger element
                if temp_sum > target: r -= 1
                # if we are below the target, increase the smaller element
                elif temp_sum < target: l += 1
                # if we are *at* the target, we have the best possible answer.
                else: return temp_sum
                ans = min(ans, temp_sum, key=lambda x: abs(target-x))
        return ans