class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r=num
        
        while r**2>num:
            r=(r+num/r)//2
        
        return r**2 == num