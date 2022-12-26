# k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    answer = 0
    num = ''
    
    while n > 0:
        n, r = divmod(n, k)
        num += str(r)
    num = num[::-1]
    
    nums = num.split('0')
    nums = [x for x in nums if x != '' and x != '1']
    for x in nums:
        if isPrime(int(x)): answer += 1

    return answer

def isPrime(n):
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0: return False
    return True
