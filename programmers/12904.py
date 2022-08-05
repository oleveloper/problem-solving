# 가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = 1
    l, r = 0, len(s)
    
    for i in range(r):
        for j in range(i + 2, r + 1):
            temp = s[i:j]
            if len(temp) < answer: continue
            if temp == temp[::-1]: answer = max(answer, j - i)
            
    return answer
