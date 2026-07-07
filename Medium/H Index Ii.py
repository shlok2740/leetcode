class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo, hi = 0, len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] < len(citations) - mid: lo = mid + 1
            else: hi = mid
        return len(citations) - lo