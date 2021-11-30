# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for v in commands:
        answer.append(sorted(array[v[0] - 1 : v[1]])[v[2] - 1])
    
    return answer
