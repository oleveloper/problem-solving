# 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    return bfs(maps)

def bfs(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    lx, ly = len(maps), len(maps[0])
    q = deque([(lx - 1, ly - 1, 1)])
    maps[lx - 1][ly - 1] = 0
    
    while q:
        x, y, cnt = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == ny == 0: 
                return cnt + 1
            elif 0 <= nx < lx and 0 <= ny < ly and maps[nx][ny] != 0:
                maps[nx][ny] = 0
                q.append([nx, ny, cnt + 1])
    
    return -1
