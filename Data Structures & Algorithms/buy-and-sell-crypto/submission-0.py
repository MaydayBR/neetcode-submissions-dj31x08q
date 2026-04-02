class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force approach O(n^2)
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                curr = prices[j] - prices[i]
                max_profit =  max(curr , max_profit)
        return max_profit