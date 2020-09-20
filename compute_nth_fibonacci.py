memo = {0: 0, 1: 1}


def fib(n):

    if n < 0:
        raise ValueError('Index must be positive')

    if n in memo:
        return memo[n]

    value = fib(n - 1) + fib(n - 2)
    # Compute the nth Fibonacci number
    memo[n] = value

    return value
