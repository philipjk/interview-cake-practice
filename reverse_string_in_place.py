# NOTE: runtime is O(n/2) so it is O(n); space complexity is O(1) because
# additional space is constant. Using lists because strings are immutable in
# python

test_list = ['a', 'e', 'i', 'o', 'u']


def reverse(inl: list) -> list:
    for i in range(len(inl)//2):
        """left = inl[i]
        inl[i] = inl[-i-1]
        inl[-i-1] = left"""
        inl[i], inl[-i-1] = inl[-1-i], inl[i]
    pass


reverse(test_list)
print(test_list)
