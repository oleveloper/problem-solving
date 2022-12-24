# 크기가 작은 부분문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    l = len(p)
    i = 0
    
    while i <= len(t) - l:
        if int(t[i : i + l]) <= int(p):
            answer += 1
        i += 1
    
    return answer
