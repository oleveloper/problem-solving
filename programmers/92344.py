# 파괴되지 않은 건물
# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    c = [[0] * (len(board[0]) + 1) for x in range(len(board) + 1)]
    
    for t, x1, y1, x2, y2, degree in skill:
        d = -degree if t == 1 else degree
        
        c[x1][y1] += d
        c[x1][y2 + 1] -= d
        c[x2 + 1][y1] -= d
        c[x2 + 1][y2 + 1] += d

    for x in range(len(board)):
        for y in range(1, len(board[0]) + 1):
            c[x][y] += c[x][y - 1]
    
    for y in range(len(board[0]) + 1):
        for x in range(1, len(board) + 1):
            c[x][y] += c[x - 1][y]
    
    return sum([1 if 0 < board[x][y] + c[x][y] else 0 for x in range(len(board)) for y in range(len(board[0]))])
