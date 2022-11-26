# 외계행성의 나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    answer = ''
    for x in str(age):
        answer += chr(int(x) + 97)
    return answer
