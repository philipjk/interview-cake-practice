
def merge_lists(l1: list, l2: list) -> list:
    merged_list = []
    while len(l1) and len(l2):
        if l1[0] <= l2[0]:
            merged_list.append(l1.pop(0))
        else:
            merged_list.append(l2.pop(0))
    while len(l1):
        merged_list.append(l1.pop(0))
    while len(l2):
        merged_list.append(l2.pop(0))
    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_lists(my_list, alices_list))

# NOTE: unrelated, but I just learned of short-circuit evaluations in python 3.6,
# which is huge: in an if statement with an and condition, the second one is
# not even evaluated if the first is false. This means that something like
# if 'becky' in friends and friends['becky'].is_free():
#    ask_her_out()
# will not throw an error if 'becky' is not in friends, even though the second
# expression cannot be evaluated
