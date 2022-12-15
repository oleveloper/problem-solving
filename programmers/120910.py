# 세균 증식
# https://school.programmers.co.kr/learn/courses/30/lessons/120910

def solution(n, t):
    for x in range(1, t + 1): n *= 2
    return n
