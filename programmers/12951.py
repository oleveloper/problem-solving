# JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    s = s.lower()
    li = s.split(' ')
    
    for v in li:
        if len(v) > 0 and v[0].isalpha(): v = v.title()
        answer += v + ' '
    
    return answer[:-1]
