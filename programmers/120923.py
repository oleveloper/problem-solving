# 연속된 수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    avg = total // num
    return [x for x in range(avg - ((num - 1)//2), avg + ((num + 2)//2))]
