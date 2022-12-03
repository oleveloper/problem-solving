# 모음 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    answer = ''
    l = ['a', 'e', 'i', 'o', 'u']
    
    for x in my_string:
        if x not in l: answer += x
    
    return answer
