# 2 x n 타일링
# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    
    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 1000000007
    
    return d[len(d) - 1]
