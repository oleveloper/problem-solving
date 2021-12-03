# 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    s = 0
    
    for i in range(count + 1):
        s += price * i
    
    answer = s - money

    if answer < 0: return 0
    else: return answer
