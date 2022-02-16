# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    answer, q = [], []
    
    for i in range(len(progresses)):
        l = 100 - progresses[i]
        q.append(math.ceil(l / speeds[i]))
    
    cnt, i = 1, 1
    prev = q[0]
    while i < len(q) + 1:
        if i == len(q):
            answer.append(cnt)
            break
        elif prev < q[i]:
            answer.append(cnt)
            cnt = 1
            prev = q[i]
        else:
            cnt += 1
        
        i += 1

    return answer
