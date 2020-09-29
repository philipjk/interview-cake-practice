
def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis

    stack = 0

    for i in range(opening_paren_index, len(sentence)):
        if sentence[i] == '(':
            stack += 1
        elif sentence[i] == ')':
            stack -= 1
            if not stack:
                return i
    if stack:
        raise ValueError('No matching parenthesis found')
