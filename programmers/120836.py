# 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836

def solution(n):
    answer, num = 0, 1
    
    while num <= n:
        x, y = divmod(n, num)
        if y == 0: answer += 1
        num += 1
    
    return answer
