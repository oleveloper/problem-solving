# 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    d = {'R':0, 'C':0, 'J':0, 'A':0, 'T':0, 'F':0, 'M':0, 'N':0}
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for idx, (x, y) in enumerate(survey):
        if choices[idx] > 4: d[y] += score.get(choices[idx])
        else: d[x] += score.get(choices[idx])

    k, v = list(d.keys()), list(d.values())
    for i in range(0, 4):
        if v[i] >= v[i + 4]: answer += k[i]
        else: answer += k[i + 4]
    
    return answer
