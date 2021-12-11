# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    d = {}
    
    for v in clothes:
        if v[1] in d: d[v[1]].append(v[0])
        else: d[v[1]] = [v[0]]
    
    for v in d.values():
        answer *= len(v) + 1
    
    return answer - 1
