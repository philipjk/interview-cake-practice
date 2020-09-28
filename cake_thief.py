

def max_duffel_bag_value(cake_tuples, weight_capacity):

    value_at_capacity = [0]*(weight_capacity + 1)
    # Calculate the maximum value we can carry
    for cake_weight, cake_value in cake_tuples:
        for capacity in range(cake_weight, weight_capacity + 1):
            delta = capacity - cake_weight
            if delta >= 0:
                value_at_capacity[capacity] = max(cake_value + value_at_capacity[delta],
                                                  value_at_capacity[capacity])

    return value_at_capacity[weight_capacity]


print(max_duffel_bag_value([(4, 4)], 12))
