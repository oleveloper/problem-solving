# 구슬을 나누는 경우의 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def solution(balls, share):
    i, j = 1, 1
    
    for x in range(balls, share, -1): i *= x
    for x in range(balls - share, 0, -1): j *= x
    
    return i // j
