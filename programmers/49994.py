# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    x, y = 0, 0
    d = {'U': (0, 1),'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    s = set()
    
    for i in dirs:
        dx, dy = x + d[i][0], y + d[i][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            s.add((x, y, dx, dy))
            s.add((dx, dy, x, y))
            x, y = dx, dy

    return len(s)//2
