class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0
        if len(prices) == 1:
            return 0
        
        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left +=1
                # right = left + 1
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
        print(maxProfit)
        return maxProfit