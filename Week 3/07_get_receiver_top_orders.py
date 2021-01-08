top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0]*len(heights)
    while heights:
        height = heights.pop()
        # 인덱스 끝에서 두번째부터 0번째까지 -1스텝씩
        # 인덱스 끝에서 두번째 : 제일 마지막에서 신호를 쏘았을 떄 수신
        # 인덱스 -1까지 : range는 시작점 이상 끝점 미만 까지기 때문에 -1까지 해야
        # 인덱스 0번 값 return
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx+1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!