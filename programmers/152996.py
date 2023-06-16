# 시소 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict

def solution(weights):
    answer = 0
    d = defaultdict(int)
    
    for w in weights:
        answer += d[w] + d[(w * 1) / 2] + d[(w * 2) / 3] + d[(w * 3) / 4] + d[w * 2] + d[(w * 3) / 2] + d[(w * 4) / 3]
        d[w] += 1

    return answer
