from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    q = deque()
    q.append((brown_loc,0))
    visited = [{} for _ in range(200001)]



    while cony_loc <= 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(q)):
            current_position, current_time = q.popleft()
            new_time = current_time +1
            new_position = current_position - 1

            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
            q.append((new_position, new_time))
            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
            q.append((new_position, new_time))
            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
            q.append((new_position, new_time))
            time += 1

            time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!