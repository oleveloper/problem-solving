# 피자 나눠 먹기 (3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    answer = slice
    while answer < n: answer += slice 
    
    return answer // slice
