# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer, w = 0, 0
    bridge = deque(0 for _ in range(bridge_length))
    
    while bridge:
        answer += 1
        w -= bridge.popleft()
        if truck_weights:
            if truck_weights[0] + w <= weight:
                bridge.append(truck_weights.pop(0))
                w += bridge[-1]
            else:
                bridge.append(0)
    
    return answer
