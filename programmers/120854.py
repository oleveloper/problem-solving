# 배열 원소의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120854

def solution(strlist):
    answer = []
    
    for x in strlist:
        answer.append(len(x))
    
    return answer
