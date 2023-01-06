# [3차] n진수 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    for x in range(0, t * m):
        answer += convert(x, n)
    return answer[p - 1::m][:t]

def convert(num, base) :
    answer = ''
    while num != 0:        
        num, r = divmod(num, base)
        if base > 10 and (10 <= r <= 16) :
            answer += "ABCDEF"[r % 10]
        else:
            answer += str(r)
    
    return '0' if answer == '' else answer[::-1]
