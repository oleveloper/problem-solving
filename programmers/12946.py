# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946

answer = []

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer

def hanoi(n, fr, to, mid):
    if n == 1: return answer.append([fr, to])

    hanoi(n - 1, fr, mid, to)
    answer.append([fr, to])
    hanoi(n - 1, mid, to, fr)
