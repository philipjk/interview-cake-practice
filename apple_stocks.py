stock_prices = [10, 7, 5, 3]


def get_max_profit(stock_prices):

    # determine best profit (sell - buy)

    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least two entries')

    min_price = stock_prices[0]
    profit = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:
        sellnow_profit = price - min_price
        profit = max(profit, sellnow_profit)
        min_price = min(price, min_price)

    return profit


# watch out for edge cases and gotchas:
# 1) empty input list is a classic
# 2) price always goes down

# an if to update a min/max can be usually substituted with just a min/max
# function

print(get_max_profit(stock_prices))
