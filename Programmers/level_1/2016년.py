def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    answer = date[(sum(month[:a - 1]) + b - 1) % 7]

    return answer