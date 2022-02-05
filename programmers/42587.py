# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])

    while len(q):
        t = q.popleft()
        if q and max(q)[0] > t[0]:
            q.append(t)
        else:
            answer += 1
            if t[1] == location: break

    return answer
