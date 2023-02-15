# 둘만의 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    a = [chr(i) for i in range(97, 123)]
    
    for c in s:
        cnt, idx = 1, index
        while cnt <= idx:
            if a[(a.index(c) + cnt) % 26] in skip: idx += 1
            cnt += 1
        answer += a[(a.index(c) + cnt) % 26 - 1]

    return answer
