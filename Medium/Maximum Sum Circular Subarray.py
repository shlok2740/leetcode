class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total=0
        maxSum, curMax=A[0],0 
        minSum, curMin=A[0],0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        