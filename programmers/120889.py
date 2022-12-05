# 삼각형의 완성조건 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120889

def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2
