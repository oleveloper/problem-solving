# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    x, y = n, m
    gcf, lcm = 1, 1
    
    while y:
        x, y = y, x % y
    
    gcf = x
    lcm = n * m // gcf
    
    answer = [gcf, lcm]
    return answer
