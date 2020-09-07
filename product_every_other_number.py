def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    if len(int_list) <= 2:
        raise ValueError('Need at least two other integers integer!')

    first_n_products = [1]
    last_n_products = [1]

    length = len(int_list)
    for i in range(0, length-1):
        first_n_products.append(first_n_products[i]*int_list[i])
        last_n_products.append(last_n_products[i]*int_list[-i - 1])

    products = []
    for i in range(0, length):
        products.append(first_n_products[i]*last_n_products[-i-1])
    return products


test = [3, 2, 1, 2, 3]

print(get_products_of_all_ints_except_at_index(test))
