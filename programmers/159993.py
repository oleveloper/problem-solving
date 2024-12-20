# 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

def bfs(start, end, maps):
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end: return dist
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and not maps[nx][ny] == 'X':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1

def solution(maps):
    answer = 0
    start, lever, exit = None, None, None
    
    for i, j in [(i, j) for i in range(len(maps)) for j in range(len(maps[0]))]:
        if maps[i][j] == 'S': 
            start = (i, j)
        elif maps[i][j] == 'L':
            lever = (i, j)
        elif maps[i][j] == 'E':
            exit = (i, j)
    
    to_lever = bfs(start, lever, maps)
    to_exit = bfs(lever, exit, maps)
    return -1 if to_lever == -1 or to_exit == -1 else to_lever + to_exit
