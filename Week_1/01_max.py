# 나의 풀이

input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    v = max(array)
    return v


result = find_max_num(input)
print(result)



# 다른 숫자들과 비교해서 찾는 방법 (이중 for문)

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)



# 지정변수 활용

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


result = find_max_num(input)
print(result)