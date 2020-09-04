def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers

    if len(list_of_ints) < 3:
        raise ValueError('The list should contain at least 3 values')

    biggest = sorted(list_of_ints[:3])
    two_smallest = sorted(list_of_ints[:3])[:2]

    for integer in list_of_ints[3:]:
        biggest = sorted(biggest + [integer])[1:]
        two_smallest = sorted(two_smallest + [integer][:2])

    big_with_neg = two_smallest[0]*two_smallest[1]*biggest[2]
    big_no_neg = biggest[0]*biggest[1]*biggest[2]
    return big_with_neg if big_with_neg > big_no_neg else big_no_neg


# WARNING: it should work with negative numbers!
