# 피자 나눠 먹기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    piece = 6
    while piece % n != 0: piece += 6
    
    return piece // 6
