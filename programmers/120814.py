# 피자 나눠 먹기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

def solution(n):
    piece = 7
    while piece < n: piece += 7
    
    return piece // 7
