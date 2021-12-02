# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    
    for x in range(500):
        if num == 1:
            answer = x
            return answer
            
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    
    answer = -1
    return answer
