message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           'h', 'o', 'm', ' ',
           's', 't', 'e', 'a', 'l']


def reverse_list(inl: list, start: int, end: int) -> list:
    for i in range((end - start)//2):
        inl[start + i], inl[end - i - 1] = inl[end - i - 1], inl[start + i]
    pass


def reverse_words(inl: list) -> list:
    reverse_list(inl, 0, len(inl))
    space_idx = [i for i in range(len(inl)) if inl[i] == ' ']
    start_idx = 0
    for i in space_idx:
        reverse_list(inl, start_idx, i)
        start_idx = i + 1
    reverse_list(inl, start_idx, len(inl))


print(message)
reverse_words(message)
print(message)
