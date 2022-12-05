# 컨트롤 제트
# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0
    l = s.split(' ')
    i = len(l) - 1
    
    while i >= 0:
        if l[i] == 'Z': i -= 1
        else: answer += int(l[i])
        i -= 1

    return answer
