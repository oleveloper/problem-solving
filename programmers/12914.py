# 멀리 뛰기
# https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    if n < 3: return n
    
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 2
    
    for x in range(3, n + 1):
        d[x] = d[x - 1] + d[x - 2]
    
    return d[n] % 1234567
