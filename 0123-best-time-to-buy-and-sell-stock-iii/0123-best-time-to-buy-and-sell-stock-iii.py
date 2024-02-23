class Solution:
    def maxProfit(self, price: List[int]) -> int:
        buy1 = -float('inf')
        sell1 = 0
        buy2 = -float('inf')
        sell2 = 0
        for p in price:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
            # print(buy1, sell1, buy2, sell2)
        return sell2