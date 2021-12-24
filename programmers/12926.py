# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    b = 26 - n
    li1 = [chr(x) for x in range(65, 91)]
    li2 = [chr(x) for x in range(97, 123)]
    
    for v in s:
        if v.isupper(): asc = ord(v) % 65
        elif v.islower(): asc = ord(v) % 97

        if v == ' ': answer += v
        elif ord(v) < 91: answer += li1[asc - b]
        else: answer += li2[asc - b]

    return answer
