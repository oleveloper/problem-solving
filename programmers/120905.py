# n의 배수 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    return [x for x in numlist if x % n == 0]
