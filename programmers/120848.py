# 팩토리얼
# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    answer = 0
    num = 1
    
    for x in range(1, 11):
        num *= x
        if num > n: break
        answer = x
            
    return answer
