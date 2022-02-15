# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer, nb = 0, 0
    b = format(n, 'b')
    
    while True:
        n += 1
        nb = format(n, 'b')
        if str(b).count('1') == str(nb).count('1'): break
    
    answer = n
    return answer
