# 개미 군단
# https://school.programmers.co.kr/learn/courses/30/lessons/120837

def solution(hp):
    answer = 0

    for i in [5, 3, 1]:
        x, hp = divmod(hp, i)
        answer += x

    return answer
