input = "토마토토마토"

# 강의 풀이 w/ 재귀함수, 문자열 슬라이싱
def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    elif len(string) == 0:
        return True
    return is_palindrome(string[1:-1])

print(is_palindrome(input))
