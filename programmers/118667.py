# 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    answer = -1
    dq1, dq2 = deque(queue1), deque(queue2)
    s1, s2 = sum(dq1), sum(dq2)
    i = 0
    while i < 300000:
        if s1 < s2:
            elem = dq2.popleft()
            s1 += elem
            s2 -= elem
            dq1.append(elem)
        elif s1 > s2:
            elem = dq1.popleft()
            s1 -= elem
            s2 += elem
            dq2.append(elem)
        else: return i
        i += 1
    
    return answer
