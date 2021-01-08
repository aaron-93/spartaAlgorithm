input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    list = ['']
    count_0 = 0
    count_1 = 0
    for i in string:
        if list[-1] != i:
            if i == "0":
                count_0 += 1
            elif i == "1":
                count_1 += 1
            list.append(i)
        elif list[-1] == i:
            list.append(i)
            pass
    return min(count_0,count_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
