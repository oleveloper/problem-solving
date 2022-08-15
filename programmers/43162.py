# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visited = [0 for x in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            dfs(visited, n, computers, i)
            answer += 1
            
    return answer


def dfs(visited, n, computers, i):
    visited[i] = 1
    
    for j in range(n):
        if i != j and computers[i][j] == 1 and visited[j] == 0:
            dfs(visited, n, computers, j)
