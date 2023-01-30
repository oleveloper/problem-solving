# 저주의 숫자 3
# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    answer = []
    i = 1
    
    while len(answer) < n:
        if i % 3 != 0 and str(i).count('3') == 0: answer.append(i)
        i += 1
            
    return answer[-1]
