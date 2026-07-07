class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        res=num%9
        return res if res>0 else 9