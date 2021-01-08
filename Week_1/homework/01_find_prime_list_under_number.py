input = 20


def find_prime_list_under_number(number):
    answer = []
    for i in range(2,number+1):
        if i == 2 or i == 3:
            answer.append(i)
        elif i%2 == 0 or i%3 == 0:
            pass
        else:
            answer.append(i)
    return answer

result = find_prime_list_under_number(input)
print(result)