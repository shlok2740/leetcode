class Solution:
    def fib(self, n: int, memo={}) -> int:
        
        if n in memo:
            return memo[n]
        if (1<= n <=2):
            return 1
        if n== 0:
            return 0
        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)
        return memo[n]