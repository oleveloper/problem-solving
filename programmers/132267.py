# 콜라 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    x = n
    while x // a > 0:
        x, y = divmod(x, a)
        x *= b
        answer += x
        x += y
    
    return answer
