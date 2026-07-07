class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        result, sumWindow = 0, 0

        for i, num in enumerate(arr):
            sumWindow += num

            if i >= k - 1:
                if sumWindow / k >= threshold:
                    result += 1
                sumWindow -= arr[i - k + 1]

        return result