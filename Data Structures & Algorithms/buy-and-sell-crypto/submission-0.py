class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        maxProfit = 0

        while True:
            if j < len(prices) - 1:
                j += 1

                maxProfit = max(maxProfit, prices[j] - prices[i])

                if prices[j] < prices[i]:
                    i = j
            else:
                return maxProfit


        