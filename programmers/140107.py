# 점 찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/140107

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        p = d ** 2 - x ** 2
        answer += (p ** (1/2)) // k + 1

    return answer
