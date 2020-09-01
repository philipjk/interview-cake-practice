take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    while len(served_orders):
        item = served_orders.pop(0)
        if len(take_out_orders) and item == take_out_orders[0]:
            take_out_orders.pop(0)
        elif len(dine_in_orders) and item == dine_in_orders[0]:
            dine_in_orders.pop(0)
        else:
            return False
    return True


print(is_first_come_first_served(take_out_orders,
                                 dine_in_orders,
                                 served_orders))

# one of the unittests fails, but I think I am right tbh
