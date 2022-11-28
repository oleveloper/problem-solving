# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

def solution(k, tangerine):
    d = dict.fromkeys(tangerine, 0)
    l = []
    
    for x in tangerine: d[x] += 1
    for x, y in sorted(d.items(), key=lambda x:x[1]):
        for i in range(y): l.append(x)
    
    return len(set(l[len(tangerine) - k:]))
