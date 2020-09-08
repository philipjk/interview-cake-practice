def find_repeat(numbers):

    # Find a number that appears more than once

    length = len(numbers)

    low = 1
    high = length - 1

    while high - low > 1:
        center = (low + high)//2

        counter = 0
        for n in numbers:
            if n > center:
                counter += 1
        if counter > (high - center):
            low = center
        elif counter <= (high - center):
            high = center
    return high


a = [1, 2, 5, 5, 5, 5]
print(find_repeat(a))

b = [4, 1, 4, 8, 3, 2, 7, 6, 5]
print(find_repeat(b))
