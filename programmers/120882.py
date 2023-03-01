# 등수 매기기
# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    answer, l = [], []
    
    for e, m in score: l.append((e + m) / 2)
    s = sorted(l, reverse = True)
    for x in l: answer.append(s.index(x) + 1)
    
    return answer
