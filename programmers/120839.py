# 가위 바위 보
# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    answer = ''
    order = ['5', '0', '2']
    
    for x in rsp:
        answer += order[order.index(x) - 1]
    
    return answer
