# 첫번째 풀이

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for idx in array:
        if answer * idx == 0 or answer:
            answer += idx
        else:
            answer *= idx
    return answer

result = find_max_plus_or_multiply(input)
print(result)

# 오답 이유 : if문의 두번째 조건식이 부적절함

# 두번째 풀이

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for idx in array:
        if answer * idx == 0 or answer * idx == answer:
            answer += idx
        else:
            answer *= idx
    return answer

result = find_max_plus_or_multiply(input)
print(result)