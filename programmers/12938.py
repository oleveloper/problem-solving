# 최고의 집합
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    if s // n == 0: return [-1]
    
    for i in range(n, 0, -1):
        answer.append(s // i)
        s -= answer[-1]
    
    return answer
