# 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    answer = ''
    
    for x in my_string:
        if x not in answer: answer += x
    
    return answer
