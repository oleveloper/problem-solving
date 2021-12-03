# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ls1, ls2, ls3 = len(s1), len(s2), len(s3)
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        if s1[i % ls1] == answers[i]:
            c1 += 1            
        if s2[i % ls2] == answers[i]:
            c2 += 1            
        if s3[i % ls3] == answers[i]:
            c3 += 1            

    maxcnt = max(c1, c2, c3)
    
    if maxcnt == c1: answer.append(1)
    if maxcnt == c2: answer.append(2)
    if maxcnt == c3: answer.append(3)
    
    return answer
