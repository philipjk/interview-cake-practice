
def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    a = 0
    for item in delivery_ids:
        a = a ^ item
    return a


id_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 7]
print(find_unique_delivery_id(id_list))
