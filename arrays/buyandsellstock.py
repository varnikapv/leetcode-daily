# DAY 1

# @Problem Buy and Sell Stock
# @description You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.
# difficulty Easy

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_price:
                max_price = profit

        return max_price
    
    

