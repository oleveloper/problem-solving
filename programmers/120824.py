# 짝수 홀수 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    even = odd = 0
    for x in num_list:
        if x % 2 == 0: even += 1
        else: odd += 1

    return [even, odd]
