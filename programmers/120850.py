# 문자열 정렬하기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120850

def solution(my_string):
    answer = []
    
    for x in my_string:
        if x.isdigit(): answer.append(int(x))
    
    return sorted(answer)
