class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # Compute F(0)
        f0 = sum(i * num for i, num in enumerate(nums))
        max_val = f0
        current = f0

        # Use recurrence relation
        for k in range(1, n):
            current = current + total_sum - n * nums[-k]
            max_val = max(max_val, current)

        return max_val

