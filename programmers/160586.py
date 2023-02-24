# 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    d = {}
    
    for k in keymap:
        for i, v in enumerate(k):
            if v in d: d[v] = min(i + 1, d.get(v))
            else: d[v] = i + 1

    for x in targets:
        cnt = 0
        for c in x:
            if c not in d:
                cnt = -1
                break
            cnt += d[c]
        answer.append(cnt)
    
    return answer
