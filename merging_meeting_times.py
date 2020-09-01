def merge_sort(inl: list) -> list:
    length = len(inl)
    if length == 1:
        return inl

    if length > 1:
        separator = length // 2
        fhalf = merge_sort(inl[:separator])
        shalf = merge_sort(inl[separator:])
        merged_list = []
        while len(fhalf) and len(shalf):
            if fhalf[0][0] <= shalf[0][0]:
                merged_list.append(fhalf.pop(0))
            else:
                merged_list.append(shalf.pop(0))
        while len(fhalf):
            merged_list.append(fhalf.pop(0))
        while len(shalf):
            merged_list.append(shalf.pop(0))
        return merged_list


def merge_meetings(ordered_meetings: list) -> list:
    start_time = ordered_meetings[0][0]
    end_time = ordered_meetings[0][1]
    merged_list = []
    for item in ordered_meetings:
        if item[0] <= end_time:
            end_time = max(item[1], end_time)
        elif item[0] > end_time:
            merged_list.append((start_time, end_time))
            start_time = item[0]
            end_time = item[1]
    merged_list.append((start_time, end_time))
    return merged_list


meeting_list = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10), (0, 3)]

print(merge_meetings(merge_sort(meeting_list)))
