class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(x) for x in nums]
        req_string=heapq.nlargest(k,nums)
        return str(req_string[-1])