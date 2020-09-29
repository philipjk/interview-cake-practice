def is_valid(code):

    # Determine if the input code is valid
    openers = set(['{', '[', '('])
    closers = set(['}', ']', ')'])

    valid = {'{': openers.union(set('}')),
             '[': openers.union(set(']')),
             '(': openers.union(set(')')),
             0: openers}

    poppers = {'{': '}', '[': ']', '(': ')', 0: 0}

    stack = [0]
    for i in range(len(code)):
        if code[i] in openers or code[i] in closers:
            if code[i] in valid[stack[-1]]:
                # either add code[i] tot he stack or pop the last item in stack
                if code[i] == poppers[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(code[i])
            else:
                return False
    if len(stack) > 1:
        return False
    return True
