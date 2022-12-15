# 문자열 정렬하기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    my_string = sorted(list(my_string.lower()))
    return ''.join(my_string)
