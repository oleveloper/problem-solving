# N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

from math import gcd

def solution(arr):
    answer = arr[0]
    
    for n in arr:
        answer *= n // gcd(answer, n)
    
    return answer
