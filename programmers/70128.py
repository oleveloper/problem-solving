# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    
    for i, v in enumerate(a):
        answer += a[i] * b[i]
    
    return answer
