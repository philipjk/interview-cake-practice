def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) <= 2:
        raise ValueError('Need at least two other integers integer!')

    length = len(int_list)
    products = []
    last = 1
    for i in range(0, length):
        products.append(last)
        last *= int_list[i]
    last = 1
    for i in range(length - 1, -1, -1):
        products[i] *= last
        last *= int_list[i]
    return products


test = [3, 2, 1, 2, 3]

print(get_products_of_all_ints_except_at_index(test))
