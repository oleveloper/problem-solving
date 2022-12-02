# 합성수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    l = []
    
    for x in range(2, n + 1):
        for y in range(2, x):
            if x % y == 0: l.append(x)

    return len(set(l))
