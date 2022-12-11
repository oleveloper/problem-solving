# 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    answer = 0
    
    while True:
        n, x = divmod(n, 10)
        answer += x
        if n == 0: break
        
    return answer
