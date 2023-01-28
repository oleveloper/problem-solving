# 안전지대
# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]
    
    boom = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: boom.append([i, j])
            
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = -1
    
    for x in board:
        answer += x.count(0)

    return answer
