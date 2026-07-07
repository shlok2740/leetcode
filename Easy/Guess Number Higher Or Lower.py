# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=(1<<31)-1
        
        while left < right:
            mid = ( left + right ) // 2
            
            g = guess(mid)
            
            if g==0:
                return mid
            elif g > 0:
                left = mid+1
            else:
                right = mid-1
                
        return left