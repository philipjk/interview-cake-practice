def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome

    letterset = {char: 0 for char in the_string}
    for char in the_string:
        letterset[char] += 1
    flag = 0
    for char in letterset.keys():
        if letterset[char] % 2:
            flag += 1
        if flag > 1:
            return False
    return True

# NOTE: runtime complexity is just O(n). Moreover, we could say that space
# complexity is O(n) because letterset is the only think taking non constant time.
# But, depending on the encoding, lettereset is bound in length by the number
# possible character representations, so 128 for ASCII and ~110000 for Unicode,
# which makes it a contant, thus O(1) in space complexity.


def has_palindrome_permutation(the_string):

    # Interview cake version
    character_set = set()
    for char in the_string:
        if char in character_set:
            character_set.remove(char)
        else:
            character_set.add(char)

    return len(character_set) <= 1
