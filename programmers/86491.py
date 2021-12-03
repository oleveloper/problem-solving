# 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    tmp = []
    wmax, hmax = 0, 0

    for w, h in sizes:
        if w > h:
            w, h = h, w
        tmp.append([w, h])
        
        if wmax < w: wmax = w
        if hmax < h: hmax = h
    
    answer = wmax * hmax
            
    return answer
