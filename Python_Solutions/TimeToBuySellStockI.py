class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float(-inf)
        min_price = float(inf)
        for i in range(len(prices)):
            min_price = prices[i] if prices[i] < min_price else min_price
            max_profit = max(max_profit, prices[i] - min_price)

        return max_profit if max_profit > 0 else 0