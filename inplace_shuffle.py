import timeit
import random

a = range(100000)


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place

    if len(the_list) <= 1:
        return

    length = len(the_list)
    for i in range(length):
        r = get_random(0, length - i - 1)
        the_list.append(the_list.pop(r))
    pass


def shuffle_ic(the_list):

    # Shuffle the input in place

    if len(the_list) <= 1:
        return

    length = len(the_list)
    for i in range(length):
        r = get_random(i, length - 1)
        the_list[i], the_list[r] = the_list[r], the_list[i]
    pass


"""fl = {key: 0 for key in range(1, 6)}

for i in range(1000000):
    a = [1, 2, 3, 4, 6]
    shuffle(a)
    for ind, k in enumerate(a):
        if k == 6:
            fl[ind + 1] += 1


print(fl)"""
