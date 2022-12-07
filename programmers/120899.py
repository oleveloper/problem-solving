# 가장 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    answer = []
    n = max(array)
    answer.append(n)
    answer.append(array.index(n))
    
    return answer
