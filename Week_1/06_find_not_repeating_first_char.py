# 첫번째 풀이

input = "abacabade"


def find_not_repeating_character(string):
    alpha_list = []

    for i in range(len(string)):
        alpha_list.append(string[i])


    for idx in range(len(alpha_list)):
        if idx in alpha_list[idx+1:]:
            pass
        else:
            return alpha_list[idx]


result = find_not_repeating_character(input)
print(result)

# 오답정리 : if idx 로 처리 -> 0은 alpha_list에 존재하지 않음. 따라서 a를 반환

# 두번째 풀이

input = "abacabade"


def find_not_repeating_character(string):
    alpha_list = []

    for i in range(len(string)):
        alpha_list.append(string[i])


    for idx in range(len(alpha_list)):
        if alpha_list[idx] in alpha_list[idx+1:]:
            pass
        else:
            return alpha_list[idx]


result = find_not_repeating_character(input)
print(result)

# 세번째 풀이

input = "abacabade"


def find_not_repeating_character(string):

    for idx in range(len(string)):
        if string[idx] in string[idx+1:]:
            pass
        else:
            return string[idx]


result = find_not_repeating_character(input)
print(result)

# 풀이설명 : 기존 string을 일일히 분해하여 비교하는 것을 없에고 바로 입력받은
# string을 쪼개어 즉석비교 (시간 복잡도 2N에서 N으로 감소)


# 강의 풀이

input = "abadabac"


def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_first_character(input)
print(result)