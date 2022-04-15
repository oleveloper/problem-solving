# 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    answer = 1 if 1 in board[0] else 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1
            if board[i][j] > answer:
                answer = board[i][j]

    return answer ** 2
