# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 1
    l = []
    
    for i in range(1, n//2 + 1):
        l.append([2 * i - 1, 2 * i])
        
    while True:
        for v in l:
            if a in v and b in v: 
                return answer
        
        tmp = []
        for i, v in enumerate(l):
            if i % 2 == 0:
                l[i] += l[i + 1]
                tmp.append(l[i])
        l = tmp
        answer += 1
        
    return answer
