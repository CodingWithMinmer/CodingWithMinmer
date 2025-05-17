def maxProfit(prices):
    min_buying_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_buying_price)

        if price < min_buying_price:
            min_buying_price = price

    return max_profit
