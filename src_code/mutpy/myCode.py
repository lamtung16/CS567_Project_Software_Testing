def find_most_common_number(arr):
    if not arr:
        return None

    most_common_num = None
    max_frequency = 0

    for i in range(len(arr)):
        current_num = arr[i]
        current_frequency = 1

        for j in range(i + 1, len(arr)):
            if arr[j] == current_num:
                current_frequency += 1

        if current_frequency > max_frequency:
            most_common_num = current_num
            max_frequency = current_frequency

    return most_common_num
