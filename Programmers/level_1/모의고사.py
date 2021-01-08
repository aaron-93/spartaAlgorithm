def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    for idx, value in enumerate(answers):
        if value == supo1[idx % len(supo1)]:
            score[0] += 1
        if value == supo2[idx % len(supo2)]:
            score[1] += 1
        if value == supo3[idx % len(supo3)]:
            score[2] += 1

    for idx, n in enumerate(score):
        if n == max(score):
            answer.append(idx + 1)
    return answer