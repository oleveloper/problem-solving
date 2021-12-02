# 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    org = x
    cnt = 0
    
    while x > 0:
        i = x % 10
        x = x // 10
        cnt += i
    
    if org % cnt == 0: answer = True
    else: answer = False
    
    return answer
