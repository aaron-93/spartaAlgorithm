def solution(s, n):
    result = ""

    for i in range(len(s)):
        char = s[i]
        if (char.isupper()):
            result += chr((ord(char) + n-65) % 26 + 65)

        elif (char.islower()):
            result += chr((ord(char) + n-97) % 26 + 97)
        else:
            result += char
    return result