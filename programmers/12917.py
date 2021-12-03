# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''
    capstr = ''
    
    for v in s[::-1]:
        if ord(v) > 64 and ord(v) < 91: capstr += v
        else: answer += v
    
    return answer + capstr
