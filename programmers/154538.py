# 숫자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    if x == y: return 0
    q = deque([[x, 0]])
    dupcheck = {}

    while q:
        x, cnt = q.popleft()
        cnt += 1

        if x in dupcheck:
            continue
        else: dupcheck[x] = 1
        
        if x + n < y:
            q.append([x + n, cnt])
        elif x + n == y: return cnt

        if x * 2 < y:
            q.append([x * 2, cnt])
        elif x * 2 == y: return cnt

        if x * 3 < y:
            q.append([x * 3, cnt])
        elif x * 3 == y: return cnt

    return -1
