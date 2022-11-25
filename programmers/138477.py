# 명예의 전당 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/138477

import heapq

def solution(k, score):
    answer, q = [], []    
    for x in score:
        heapq.heappush(q, x)
        answer.append(heapq.nlargest(k, q)[-1])
    
    return answer
