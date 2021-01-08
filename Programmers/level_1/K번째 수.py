def solution(array, commands):
    answer = []

    for cmd in commands:
        start = cmd[0] - 1
        end = cmd[1]
        val = cmd[2] - 1

        a = array[start:end]
        a.sort()
        answer.append(a[val])

    return answer