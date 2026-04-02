class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        greatest_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                curr = prices[i] - lowest
                greatest_profit = max(greatest_profit, curr)
        return greatest_profit