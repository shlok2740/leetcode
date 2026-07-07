class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = inf, 0
        for x in prices:
            buy =  min(buy, x - sell)
            sell = max(sell, x - buy - fee)
        return sell