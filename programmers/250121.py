# [PCCE 기출문제] 10번 / 데이터 분석
# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    col = ["code", "date", "maximum", "remain"]
    idx = col.index(ext)
    
    answer = [x for x in data if x[idx] < val_ext]
    answer = sorted(answer, key=lambda x : x[col.index(sort_by)])
    
    return answer
