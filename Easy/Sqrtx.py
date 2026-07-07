class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0,1]:
            return x

        left = 0
        right = x - 1
        middle = left + (right - left) // 2

        while left <= right:
            if middle ** 2 < x:
                left = middle + 1
            elif middle ** 2 > x:
                right = middle - 1
            else:
                return middle
            middle = left + (right - left) // 2
        return middle