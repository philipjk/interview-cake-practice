
def fib(n):

    if n < 0:
        raise ValueError('Index must be positive')

    last = 1
    second_last = 0

    if n == 1:
        return last
    if n == 0:
        return second_last

    for i in range(2, n + 1):
        second_last, last = last, last + second_last

    # Compute the nth Fibonacci number

    return last
