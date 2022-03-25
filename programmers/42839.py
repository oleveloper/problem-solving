# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    s = set()
    
    for i in range(len(numbers)):
        s |= set(map(int, map("".join, permutations(numbers, i + 1))))
        
    s -= set(range(0, 2))
    n = int(max(s) ** 0.5)

    for i in range(2, n):
        s -= set(range(i * 2 , max(s) + 1, i))

    return len(s)
