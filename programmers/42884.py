# 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 1
    routes.sort(reverse=True, key = lambda x: x[0])
    r = routes[0][0]
    
    for i in routes[1:]:
        if i[1] >= r:
            continue
        else:
            r = i[0]
            answer += 1
    
    return answer
