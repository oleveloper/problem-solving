# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    triad = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        triad += str(mod)
    
    answer = int(triad, 3)
    return answer
