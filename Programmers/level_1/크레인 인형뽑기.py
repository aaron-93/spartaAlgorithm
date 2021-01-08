def solution(board, moves):
    basket = []
    ans = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] > 0:
                basket.append(board[j][i - 1])
                board[j][i - 1] = 0
                if basket[-1:] == basket[-2:-1]:
                    ans += 2
                    basket = basket[:-2]
                break
    return ans