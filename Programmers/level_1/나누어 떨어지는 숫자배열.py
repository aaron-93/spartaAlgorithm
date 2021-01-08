def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
        elif i%divisor != 0:
            continue
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer