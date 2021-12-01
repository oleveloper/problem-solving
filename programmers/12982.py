# 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    s = 0

    d.sort()
    for v in d:
        if s + v <= budget:
            s += v
            answer += 1
    
    return answer
