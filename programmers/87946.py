# 피로도
# https://programmers.co.kr/learn/courses/30/lessons/87946

answer = 0
dungeons_len = 0
visited = []

def dfs(k, dungeons, start):
    global answer
    
    if start > answer: answer = start

    for i in range(dungeons_len):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, start + 1)   
            visited[i] = False
            
def solution(k, dungeons):
    global visited, dungeons_len
    dungeons_len = len(dungeons)
    visited = [False] * dungeons_len
    
    dfs(k, dungeons, 0)
    return answer
