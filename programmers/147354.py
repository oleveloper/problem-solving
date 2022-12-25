# 테이블 해시 함수
# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    d = sorted(data, key = lambda x : (x[col - 1], -x[0]))
    s = 0
    
    for i in range(row_begin - 1, row_end):
        m = 0
        for j in d[i]: m += j % (i + 1)
        s = s ^ m
    
    return s
