# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    start = 1
    
    while start <= n:
        s = 0
        for i in range(start, n + 1):
            s += i
            if s > n:
                start += 1
                break
            elif s == n:
                start += 1
                answer += 1
                break

    return answer
