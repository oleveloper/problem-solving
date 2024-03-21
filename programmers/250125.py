# [PCCE 기출문제] 9번 / 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    
    for i in range(0, 4):
        h_check, w_check = h + dh[i], w + dw[i]
        if n > h_check >= 0 and n > w_check >= 0 and board[h][w] == board[h_check][w_check]:
            count += 1
    
    return count
