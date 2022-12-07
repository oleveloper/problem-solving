# 문자열 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    answer = 0
    l = my_string.split(' ')
    o = ''
    
    for x in l:
        if x.isdigit(): 
            if o == '+': answer += int(x)
            elif o == '-': answer -= int(x)
            else: answer = int(x)
        else: o = x

    return answer
