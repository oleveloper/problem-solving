# 직사각형 넓이 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    answer = (max(x) - min(x)) * (max(y) - min(y))
    
    return answer
