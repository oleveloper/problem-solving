# 마법의 엘리베이터
# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer, i = 0, 0
    l = [int(x) for x in str(storey)[::-1]] + [0]
    
    while i < len(l):
        if l[i] > 5:
            l[i + 1] += 1
            answer += 10 - l[i]
        else:
            if l[i] == 5: l[i + 1] += 1 if l[i + 1] >= 5 else 0
            answer += l[i]
        i += 1

    return answer
