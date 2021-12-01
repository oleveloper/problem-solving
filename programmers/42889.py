# 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    s = [0 for x in range(N)]
    r = [0 for x in range(N)]
    p = len(stages)
    temp = []
    
    for v in stages:
        if v <= N: s[v - 1] += 1
    
    for i, v in enumerate(s):
        if p == 0: r[i] = 0.0
        else : r[i] = v / p
        p -= v
        temp.append([r[i], i + 1])

    temp.sort(key = lambda x : x[0], reverse=True)
    answer = [x[1] for x in temp] 
    
    return answer
