
current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dr = [-1, 0, 1, 0]
dc = [0,1,0,-1]

def rotation_left(d):
    return (d+3) %4

def move_backward(d):
    return (d+2)%4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    answer = 1
    room_map[r][c] =2
    q = list([[r,c,d]])

    while q:
        r,c,d = q.pop(0)
        temp_d = d

        for i in range(4):
            temp_d = rotation_left(temp_d)
            new_r, new_c = r + dr[temp_d],  c+ dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                answer += 1
                room_map[new_r][new_c] =2
                q.append([new_r,new_c,temp_d])
                break
            elif i == 3:
                new_r, new_c = r+dr[move_backward(temp_d)], c+dc[move_backward(temp_d)]
                q.append([new_r,new_c,temp_d])
                if room_map[new_r][new_c] == 1:
                    return answer

    return

#
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
