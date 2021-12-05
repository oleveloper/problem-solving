# 소수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations

def calculate(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True

def solution(nums):
    answer = 0

    l = list(combinations(nums, 3))
    for v in l:
        if calculate(sum(v)): answer += 1
            
    return answer
