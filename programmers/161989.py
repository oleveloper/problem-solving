# 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer, i = 0, 0
    l = [i + 1 for i in range(section[-1] + 1)]
    for s in section:
        l[s - 1] = -1
    
    while i < len(l):
        if l[i] == -1:
            i += m
            answer += 1
        else:
            i += 1
    
    return answer
