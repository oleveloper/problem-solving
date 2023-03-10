# 롤케이크 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

def solution(topping):
    answer = 0
    d1 = {}
    for x in topping:
        if x in d1: d1[x] += 1
        else: d1[x] = 1
    d2 = {}

    for x in topping:
        d1[x] -= 1
        if x not in d2:
            d2[x] = 1

        if d1[x] == 0: 
            del d1[x]

        if len(d1) == len(d2):
            answer += 1

    return answer
