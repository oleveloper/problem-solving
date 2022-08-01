# 야근 지수
# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    
    for _ in range(n):
        item = heapq.heappop(works) + 1
        heapq.heappush(works, item)
    
    return sum([x ** 2 for x in works if x < 0])
