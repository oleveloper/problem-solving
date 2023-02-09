# 평행
# https://school.programmers.co.kr/learn/courses/30/lessons/120875

from itertools import combinations

def solution(dots):
    answer = []
    
    for dot1, dot2 in list(combinations(dots, 2)):
        answer.append(slopee(dot1, dot2))
    
    return 1 if (len(answer) - len(set(answer))) > 0 else 0

def slopee(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return (y2 - y1) / (x2 - x1)
