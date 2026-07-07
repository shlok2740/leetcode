class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        self.piles = piles
        ans = self.binarySearch(h)
        return ans
              
            
    def binarySearch(self,h):
        l, r = 1, max(self.piles)
        while l < r:
            m = l + (r-l) // 2
            time = self.eatingTime(m)
            if time > h:
                l = m + 1
            else:
                r = m
        return l
        
    def eatingTime(self,k):  # return at current speed k, how much time needed to eat all the piles in the list
        time = 0
        for i in self.piles:
            curTime = ceil(i / k) 
            time += curTime
        return time