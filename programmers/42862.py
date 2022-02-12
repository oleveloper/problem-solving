# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    
    dup = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(dup))
    reserve = list(set(reserve) - set(dup))
    
    lost.sort()
    reserve.sort()
    
    d = dict.fromkeys(lost, 0)
    for r in reserve:
        if r - 1 in d: del d[r - 1]
        elif r + 1 in d: del d[r + 1]
        elif r in d: del d[r]

    answer += n - len(d)
    return answer
