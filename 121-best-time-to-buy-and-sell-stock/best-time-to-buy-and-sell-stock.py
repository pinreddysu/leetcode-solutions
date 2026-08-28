class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,0

        maxProfit = 0

        if len(prices) ==1:
            return maxProfit

        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i+=1
            else:
                maxProfit = max(maxProfit, prices[j] - prices[i])
                j+=1
        return maxProfit

        