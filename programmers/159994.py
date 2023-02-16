# 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque

def solution(cards1, cards2, goal):
    q, q1, q2 = deque(goal), deque(cards1), deque(cards2)
    c1, c2 = q1.popleft(), q2.popleft()
    
    while q: 
        c = q.popleft()
        if c == c1 and q1:
            c1 = q1.popleft()
        elif c == c2 and q2:
            c2 = q2.popleft()
        elif c != c1 and c != c2: 
            return 'No'

    return 'Yes'
