# 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    return 1 if float.is_integer(n ** (1 / 2)) else 2
