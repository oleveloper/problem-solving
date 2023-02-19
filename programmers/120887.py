# k의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120887

def solution(i, j, k):
    answer = 0
    
    for n in range(i, j + 1):
        answer += int(str(n).count(str(k)))
    
    return answer
