# 유한소수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def solution(a, b):
    n = b // gcd(a, b)
    
    while True:
        if n % 2 == 0:
            n //= 2
        elif n % 5 == 0:
            n //= 5
        else:
            break
    
    return 1 if n == 1 else 2

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
