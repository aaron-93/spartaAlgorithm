input = [4, 6, 2, 9, 1]

# 내가 처음 작성한 코드, 실패
# def bubble_sort(array):
#     for i in range(len(array)):
#         cur = array[i]
#         comp = array[i+1]
#         while comp is not None:
#             if comp > cur:
#                 cur, comp = comp, cur
#
#     return array


# bubble_sort(input)
# print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!


# 강의 코드

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
