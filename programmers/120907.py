# OX퀴즈
# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    
    for q in quiz:
        x = q.split("=")
        if eval(x[0]) == int(x[1]): answer.append("O")
        else: answer.append("X")
    
    return answer
