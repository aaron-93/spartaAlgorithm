# 나의 풀이

s = "(())()"

# 큐 생성
q = []


def is_correct_parenthesis(string):
    # 입력받은 string을 쪼개어 큐에 삽입
    for p in string:
     # 올바른 괄호는 ( 으로 시작해서 )으로 끝나기 때문에 무조건 (으로 시작하여야 함. 따라서 (는 큐에 무조건 삽입
        if p == '(':
            q.append(p)
        else:
        # 큐에 삽입하려고 하는 값이 ) 일 경우
            try:
                #큐에 ( 기호가 있는지 확인 후 있다면 ( 기호 삭제
                q.pop()
            except:
                # 큐에 ( 기호가 없다면 올바른 괄호를 만들 수 없음으로 False 반환
                return False
    # 모든 값을 다 삽입해서 올바른 괄호로 모두 만들 수 있다면 큐의 길이는 0
    if len(q) == 0:
        # 따라서 큐의 길이가 0이라면 True 반환
        return True
        # ( 기호가 남아있다면 False 반환
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!


# 강의 풀이 1

s = "(())()"



def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False



print(is_correct_parenthesis(s))
