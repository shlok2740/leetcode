class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = -1
        for rectangle in rectangles:
            maxLen = max( min(rectangle), maxLen )
        
        ans = 0
        for rectangle in rectangles:
            if min(rectangle) == maxLen: ans += 1
                
        return ans