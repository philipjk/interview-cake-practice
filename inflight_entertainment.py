# This is an interesting one: there are three possible solutions presented here,
# following what's on the website.

# 1) One is using brute force solution. We take the first film duration, and see
# what the difference is with the flight duration. This value needs to be checked
# against every other film duration to see which one matches. By repeating for
# every first film duration, we get a runtime complexity of O(n^2), and O(1) space.


import unittest


def brute_force(movie_lengths, flight_length):
    for i, first_movie in enumerate(movie_lengths):
        remaining_time = flight_length - first_movie
        for j, second_movie in enumerate(movie_lengths):
            if remaining_time == second_movie and i != j:
                return True
    return False

# 2) Two is using merge sort and binary search. The first looping over movie_length
# is needed. The second loop, however can be substituted by a binary search over
# a sorted array which takes O(log(n)), thus giving us O(nlog(n)).
# Sorting the array is still O(nlog(n)) so the overall time complexity is O(nlog(n)).
# Space complexity of merge-sort is O(n) while only O(1) for binary search for a
# total of O(n) space complexity.

# NOTE: STILL FAILING A TEST!!!!


def merge_sort(inl: list) -> list:
    length = len(inl)

    if length <= 1:  # leq and not eq to account for empty input lists
        return inl

    first_half = merge_sort(inl[:length//2])
    second_half = merge_sort(inl[length//2:])
    merged_list = []

    while len(first_half) and len(second_half):
        if first_half[0] <= second_half[0]:
            merged_list.append(first_half.pop(0))
        else:
            merged_list.append(second_half.pop(0))
    while len(first_half):
        merged_list.append(first_half.pop(0))
    while len(second_half):
        merged_list.append(second_half.pop(0))
    return merged_list


def binary_search_recursive(inl: list, item: int) -> bool:
    # NOTE: runtime O(log(n)), space O(1)
    if len(inl) == 1 and inl[0] == item:
        return True
    if len(inl) == 1 and inl[0] != item:
        return False
    half_idx = len(inl)//2
    if item >= inl[half_idx]:
        return binary_search_recursive(inl[half_idx:], item)
    else:
        return binary_search_recursive(inl[:half_idx], item)


def binary_search_iterative(inl: list, item: int) -> int:
    floor_index = 0
    ceiling_index = len(inl) - 1
    while floor_index < ceiling_index:
        half_index = (ceiling_index + floor_index) // 2
        if item == inl[half_index]:
            return True
        elif item > inl[half_index]:
            floor_index = half_index + 1
        else:
            ceiling_index = half_index
    return False


def sort_and_search(movie_lengths, flight_length):
    sorted_movie_lengths = merge_sort(movie_lengths)
    for first_movie in sorted_movie_lengths:
        spare = flight_length - first_movie
        if spare > 0:
            # bsi = binary_search_iterative(sorted_movie_lengths,
            #                               spare)
            bsr = binary_search_recursive(sorted_movie_lengths,
                                          spare)
            # assert bsi == bsr
            if bsr and first_movie:
                return True
    return False

# 3) Three is through the use of hash maps. In particular, using sets we can
# reduce the second loop to O(1) runtime complexity at the cost of increasing
# space complexity to O(n).


def hashed_search(movie_lengths, flight_length):
    movie_lengths_seen = set()

    for first_movie in movie_lengths:
        second_movie = flight_length - first_movie
        if second_movie in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie)
    return False
