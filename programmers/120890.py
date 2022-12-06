# 가까운 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.sort()
    a = [(x - n) ** 2 for x in array]
    return array[a.index(min(a))]
