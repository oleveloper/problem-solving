# 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))
    
    for i in photo:
        point = 0
        for j in i:
            point += d.get(j, 0)
        answer.append(point)
        
    return answer
