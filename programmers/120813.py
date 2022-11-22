# 짝수는 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    return [i - 1 for i in range(2, n + 2, 2)]
