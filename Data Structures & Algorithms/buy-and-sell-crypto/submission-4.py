class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start_ptr = 0
        end_ptr = start_ptr + 1
        max_profit = 0

        while end_ptr < len(prices):
           
            if prices[start_ptr] < prices[end_ptr]:
                current_profit = prices[end_ptr] -  prices[start_ptr]
                max_profit = max(max_profit,current_profit )
            else:
                start_ptr = end_ptr
            end_ptr += 1
        return max_profit

        