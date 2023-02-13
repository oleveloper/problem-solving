# 멀쩡한 사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    answer = w * h
    n = min(w, h)
    gcd = []
    
    for i in range(1, n + 1):
        if w % i == 0 and h % i == 0:
            gcd.append(i)

    answer -= (w + h) - max(gcd)
    return answer
