def find_rotation_point(words):

    # Find the rotation point in the list

    length = len(words)
    if length < 2:
        raise ValueError("It needs more than 1 element")

    low_idx = 0
    high_idx = length - 1

    while high_idx - low_idx > 1:
        current_idx = (low_idx + high_idx)//2
        if words[current_idx] < words[low_idx]:
            high_idx = current_idx
        elif words[current_idx] > words[low_idx]:
            low_idx = current_idx
    return high_idx
