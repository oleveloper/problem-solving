# 옷가게 할인 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/120818

def solution(price):
    ratio = 0
    if price >= 500000:
        ratio = 0.2
    elif price >= 300000:
        ratio = 0.1   
    elif price >= 100000:
        ratio = 0.05

    return int(price - price * ratio)
