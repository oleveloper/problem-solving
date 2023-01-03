# 캐릭터의 좌표
# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    x, y = 0, 0
    d = {"left": (-1, 0), "right": (1, 0), "up": (0, 1), "down": (0, -1)}
    
    for k in keyinput:
        dx, dy = d.get(k)
        if abs(x + dx) <= board[0] // 2 and abs(y + dy) <= board[1] // 2:
            x += dx
            y += dy

    return [x, y]
