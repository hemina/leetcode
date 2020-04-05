"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

@author Mina HE
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        s = 0
        buy_price = prices[0]
        sell_price = min(prices)

        for i in range(1, len(prices)):
            # if prices[i] > buy_price, buy at buy_price, earn prices[i]-buy_price
            # otherwise, set buy_price at prices[i], earn 0
            # if prices[i] <= price[i-1], sell at price[i-1]
            # otherwise, set sell_price at prices[i]
            if i == len(prices) - 1 and prices[i] >= prices[i - 1]:
                s += prices[i] - buy_price
            if buy_price < prices[i]:  # when we bought at buy_price, not at prices[i], we may set sell_price from now
                sell_price = max(prices[i], prices[i - 1])
            if sell_price > prices[i]:  # when prices[i] < price[i-1], we sell at price[i-1]
                s += sell_price - buy_price
                buy_price = prices[i]
                sell_price = prices[i]
            buy_price = min(prices[i], buy_price)
        return s


"""
Runtime: 60 ms, faster than 76.77% of Python online submissions.
Memory Usage: 15.3 MB, less than 7.32% of Python online submissions.
Complexity: O(n)
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        s = 0
        for i in range(len(prices)-1):
            s += max(prices[i+1]-prices[i], 0)
        return s


"""
Runtime: 48 ms, faster than 99.72% of Python online submissions.
Memory Usage: 15.2 MB, less than 7.32% of Python online submissions.
Complexity: O(n)
"""
