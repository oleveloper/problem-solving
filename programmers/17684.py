# [3차] 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    d = {chr(ord('A') + i) : i + 1 for i in range(0, 26)}
    s = ''
    
    for i, v in enumerate(msg):
        s += v
        if s not in d:
            answer.append(d[s[:-1]])
            d[s] = len(d) + 1
            s = s[-1]

        if i == len(msg) - 1:
            answer.append(d[s])

    return answer
