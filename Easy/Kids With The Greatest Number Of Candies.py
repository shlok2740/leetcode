class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[False]*(len(candies))
        large=max(candies)
        for i ,x in enumerate(candies):
            if x+extraCandies>=large:
                res[i]=True
                
        return res