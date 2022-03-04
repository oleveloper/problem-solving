# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    tile = brown + yellow
    
    for w in range(1, brown):
        for h in range(1, w + 1):
            if tile == w * h and w * 2 + h * 2 - 4 == brown:
                answer.append(w)
                answer.append(h)
                return answer
