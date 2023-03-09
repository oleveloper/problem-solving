# 문자열 밀기
# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    if A == B: return 0
    l = list(A)
    
    for i in range(len(A)):
        l = l[-1:] + l[:-1]
        if ''.join(l) == B: 
            return i + 1

    return -1
