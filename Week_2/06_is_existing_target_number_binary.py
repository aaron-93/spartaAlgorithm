finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    min_point = 0
    max_point = len(finding_numbers)-1
    center_point = (min_point + max_point) //2

    while min_point <= max_point:
        if array[center_point] == target:
            return True
        elif array[center_point] < target:
            min_point = center_point + 1
        else:
            max_point = center_point -1
        center_point = (min_point + max_point) //2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)