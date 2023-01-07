# 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    answer = 1

    for i in range(2, number + 1):
        cnt = 0
        for j in range(1, int(i ** (1/2)) + 1):
            if i % j == 0:
                if j == i // j: cnt += 1
                else: cnt += 2
        answer += power if cnt > limit else cnt

    return answer
