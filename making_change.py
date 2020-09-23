memo = {}


def recursive(amount, coins):
    print(f'Checking ways to make {amount} with {coins}')
    count = 0
    global memo

    if str((amount, coins)) in memo:
        print('Fetched from memo')
        return memo[str((amount, coins))]

    p = amount // coins[0]

    for i in range(p, -1, -1):
        if i*coins[0] == amount:
            count = count + 1
        if i*coins[0] < amount:
            delta = amount - i*coins[0]
            if len(coins) > 1:
                count += recursive(delta, coins[1:])
    memo[str((amount, coins))] = count
    return count


def change_possibilities(amount, denominations):
    if not len(denominations):
        return 0
    value = recursive(amount, denominations)

    return value


print(change_possibilities(4, [3, 1, 2]))
