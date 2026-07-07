class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)): return 0
        for i in range(left+1, right+1):
            left = left & i
        return left