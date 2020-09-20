

def find_permutations(parent_substring, children_substring):
    permutation_set = set()

    if len(children_substring) == 1:
        # print(parent_substring + children_substring)
        permutation_set.add(parent_substring + children_substring)
        return permutation_set
    if not len(children_substring):
        return ''

    for i in range(len(children_substring)):
        result = find_permutations(parent_substring + children_substring[i],
                                   children_substring[:i] + children_substring[i+1:])
        for item in result:
            permutation_set.add(item)
    return permutation_set


print(find_permutations('', 'abc'))
