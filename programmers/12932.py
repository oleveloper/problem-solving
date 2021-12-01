# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    
    while n > 0:
        answer.insert(0, n % 10)
        n //= 10
    
    answer.reverse()
    return answer
