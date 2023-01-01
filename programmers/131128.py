# 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128

def solution(X, Y):
    answer = ''
    dx, dy = {}, {}
    for x in X: dx[x] = dx.get(x, 0) + 1
    for y in Y: dy[y] = dy.get(y, 0) + 1

    for kx, vx in sorted(dx.items(), reverse=True):
        if kx in dy.keys(): answer += kx * min(vx, dy[kx])

    if answer.isdigit() == False: return '-1'
    elif len(answer) == answer.count('0'): return '0'
    else: return answer
