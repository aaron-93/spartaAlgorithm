input = "소주만병만주소"

# 나의 풀이
def is_palindrome(string):
    l = len(string)
    for i in range(l):
        if string[i] != string[-1-i]:
            return False
    return True


print(is_palindrome(input))


