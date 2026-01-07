class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        k = 1
        while k < len(prices):
            if prices[i] > prices[k]:
                k += 1
                i = k - 1
            else:
                curr_profit = prices[k] - prices[i] 
                if curr_profit > profit:
                    profit = curr_profit
                k += 1
        return profit

  # Runtime: Beats 75%
