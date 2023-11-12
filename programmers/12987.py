# 숫자 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer, i = 0, 0
    A.sort()
    B.sort()

    for a in A:
        while i < len(B) and B[i] <= a:
            i += 1

        if i < len(B):
            answer += 1
            i += 1

    return answer
