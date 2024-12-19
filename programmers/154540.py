# 무인도 여행
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def bfs(x, y, maps, visited):
    queue = deque([(x, y)])
    total = 0
    visited[x][y] = True
    
    while queue:
        cx, cy = queue.popleft()
        total += int(maps[cx][cy])
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[1]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return total

def solution(maps):
    m = maps
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for i, j in [(i, j) for i in range(len(maps)) for j in range(len(maps[0]))]:
        if maps[i][j] == 'X' or visited[i][j]: continue
        answer.append(bfs(i, j, maps, visited))

    return sorted(answer) if len(answer) > 0 else [-1]
