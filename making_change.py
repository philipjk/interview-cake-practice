
def change_possibilities(amount, denominations):
    if not len(denominations):
        return 0
    C = [0]*(amount + 1)
    C[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            delta = higher_amount - coin
            C[higher_amount] += C[delta]
    return C[amount]


print(change_possibilities(50, [5, 10]))
