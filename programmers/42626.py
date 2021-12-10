# 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        min1 = heapq.heappop(scoville)
        
        if  min1 >= K: break
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2 * 2)
        answer += 1
    
    if scoville[0] > K: return answer
    else: return -1
