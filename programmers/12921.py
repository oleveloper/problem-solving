# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    sieve = [False, False] + [True] * (n - 1)
    primes = []
    
    for i in range(2, n + 1):
        if sieve[i]: 
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                sieve[j] = False

    answer = sieve.count(True)
    return answer
