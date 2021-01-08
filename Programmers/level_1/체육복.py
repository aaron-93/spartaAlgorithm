def solution(n, lost, reserve):
    list = []
    checker = [[2, 0], [0, 2]]

    for idx in range(n):
        list.append(1)
    for idx in reserve:
        list[idx - 1] += 1
    for idx in lost:
        list[idx - 1] += -1

    for idx in range(len(list)):
        if list[idx:idx + 2] in checker:
            list[idx] = 1
            list[idx + 1] = 1

    while 0 in list:
        list.remove(0)
    answer = len(list)
    return answer