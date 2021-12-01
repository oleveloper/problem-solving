# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = 0
    root = n ** (1/2)
    
    if root.is_integer():
        answer = (root + 1) ** 2
    else:
        answer = -1
    
    return answer
