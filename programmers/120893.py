# 대문자와 소문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    
    for x in my_string:
        answer += x.lower() if x.isupper() else x.upper()

    return answer
