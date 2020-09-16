
def find_duplicate(int_list):

    # Find a number that appears more than once ... in O(n) time

    for i in range(len(int_list)):
        if i + 1 != int_list[i]:
            initial_value = int_list[i]
            new_value = int_list[initial_value - 1]
            break

    while new_value != initial_value:
        new_value = int_list[new_value - 1]

    return new_value
