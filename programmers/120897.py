# 약수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120897

def solution(n):
    answer = []
    i = 0
    
    while i <= n:
        i += 1
        if n % i == 0: answer.append(n // i)
    
    return sorted(answer)
