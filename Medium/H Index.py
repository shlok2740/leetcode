class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l=0
        r=len(citations)
        
        while l<r:
            mid=(l+r)//2
            
            if citations[mid]<len(citations)-mid:
                l=mid+1
            else:
                r=mid
                
        return len(citations)-l