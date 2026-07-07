class Solution:
    def computeArea(self, left1, bottom1, right1, top1, left2, bottom2, right2, top2):
        first = (right1 - left1) * (top1 - bottom1)
        second = (right2 - left2) * (top2 - bottom2)
        
        left    = max(left1, left2)
        right   = min(right1, right2)
        top     = min(top1, top2)
        bottom  = max(bottom1, bottom2)
        
        width   = max(right - left, 0)
        height  = max(top - bottom, 0)
        
        overlap = width * height
        
        return first + second - overlap