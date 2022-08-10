# [카카오 인턴] 수식 최대화
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations

def solution(expression):
    answer = []
    
    for x, y, z in list(permutations(['*', '+', '-'])):
        templist = []
        for i in expression.split(x):
            temp = [f'({j})' for j in i.split(y)]
            templist.append(f'({y.join(temp)})')
        answer.append(abs(eval(x.join(templist))))
    
    return max(answer)
