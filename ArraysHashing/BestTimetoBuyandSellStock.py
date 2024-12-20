class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit,price - buy)
            buy = min(buy,price)
        return maxProfit