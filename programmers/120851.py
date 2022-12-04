# 숨어있는 숫자의 덧셈 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    answer = 0
    
    for x in my_string:
        if x.isdigit(): answer += int(x)
    
    return answer
