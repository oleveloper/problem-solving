# 연속 부분 수열 합의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = []
    e = elements * 2
    
    for i in range(1, len(elements) + 1):
        for j in range(0, len(elements) + 1):
            answer.append(sum(e[j : i + j]))
    
    return len(set(answer))
