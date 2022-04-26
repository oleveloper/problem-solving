# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = [[0 for i in range(1, j + 1)] for j in range(1, n + 1)]
    answer[0][0] = 1
    x, y = -1, 0
    cnt = 1
    
    for i in range(0, n):
        for j in range(i, n):
            if i % 3 == 0: x += 1
            elif i % 3 == 1: y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            answer[x][y] = cnt            
            cnt += 1            
            
    answer = sum(answer, [])
    return answer
