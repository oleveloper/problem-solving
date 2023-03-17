# 삼각형의 완성조건 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120868

def solution(sides):
    answer = 0
    a, b = sorted(sides)
    
    c = b - a
    for i in range(c + 1, b + 1):
        answer += 1    
    for c in range(b + 1, a + b):
        answer += 1

    return answer
