# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    p = [_ for _ in range(1, n + 1)]
    used = [words[0]]
    idx = 1

    while idx < len(words):
        if words[idx - 1][-1] != words[idx][0] or words[idx] in used:
            turn = p[(idx + 1) % n - 1]
            time = idx // n + 1
            return [turn, time]
        used.append(words[idx])
        idx += 1
        
    return [0, 0]
