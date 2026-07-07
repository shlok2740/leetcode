class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        total = 0
        
        while z != 0:
            if (z & 1):
                total += 1
            z = z // 2
        
        return total