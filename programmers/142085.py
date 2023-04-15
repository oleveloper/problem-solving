# 디펜스 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/142085

from heapq import heappush, heappop

def solution(n, k, enemy):
    q = []
    
    for i, v in enumerate(enemy):
        heappush(q, v)
        if len(q) > k:
            n -= heappop(q)
        if n < 0: 
            return i

    return len(enemy)
