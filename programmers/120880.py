# 특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    answer = []
    d = {}
    for num in numlist:
        d[num] = abs(n - num)
    
    for k, v in (sorted(d.items(), key = lambda x: (x[1], -x[0]))):
        answer.append(k)
    
    return answer
