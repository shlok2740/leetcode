class Solution:
    def numSquares(self, n: int) -> int:
        candidates = set([i * i for i in range(1, int(n**0.5)+1)])
        
        def divisible(n, count):
            if count == 1:
                return n in candidates
            for num in candidates:
                if divisible(n-num, count-1):
                    return True
            return False

        for count in range(1, n+1):
            if divisible(n, count):
                return count