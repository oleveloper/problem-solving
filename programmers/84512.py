# 모음 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = []
    l = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        for j in product(l, repeat=i):
            answer.append(''.join(j))

    return sorted(answer).index(word) + 1
