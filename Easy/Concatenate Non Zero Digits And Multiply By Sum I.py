class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new_num, sum_num = 0, 0
        multiplier = 1

        while n:
            d = n % 10
            if d != 0:
                new_num += d * multiplier
                multiplier *= 10
                sum_num += d
            n //= 10

        return new_num * sum_num

