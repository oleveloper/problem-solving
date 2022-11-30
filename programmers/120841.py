# 점의 위치 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    answer = 0
    
    x, y = dot
    if x > 0 and y > 0: answer = 1
    elif x < 0 and y > 0: answer = 2
    elif x < 0 and y < 0: answer = 3
    elif x > 0 and y < 0: answer = 4

    return answer
