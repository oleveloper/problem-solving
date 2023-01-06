# 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    q = [x for x in range(1, order[0])]
    answer, i, j = 0, 0, len(q) + 1

    while i < len(order):
        if len(q) and q[-1] == order[i]:
            q.pop(-1)
            answer += 1
            i += 1
        elif len(q) and q[-1] > order[i]: 
            break
        else:
            q.append(j)
            j += 1

    return answer
