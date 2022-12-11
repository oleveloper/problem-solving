# 가장 가까운 같은 글자
# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    d = dict.fromkeys([x for x in s], -1)
    
    for i, v in enumerate(s):
        if d[v] != -1:
            answer.append(i - d[v])
            d[v] = i
        else: 
            answer.append(-1)
        d[v] = i
    
    return answer
