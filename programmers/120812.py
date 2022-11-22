# 최빈값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    if len(array) == 1: return array[0]

    d = {i : array.count(i) for i in set(array)}
    m = max(d.values())
    l = [k for k, v in d.items() if v == m]
    
    return -1 if len(l) > 1 else l[0]
