# 과일 장수
# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    
    score.sort()
    score = score[len(score) % m:]

    for x in score[::m]:
        answer += x * m
    
    return answer
