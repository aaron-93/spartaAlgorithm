numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    list = [0]
    for i in array:
        cal_list = []
        for j in list:
            cal_list.append(j+1)
            cal_list.append(j-1)
        list = cal_list

    return list.count(target)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!