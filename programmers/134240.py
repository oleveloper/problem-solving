# 푸드 파이트 대회
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for i, v in enumerate(food[1:]): 
        for j in range(v // 2): answer += str(i+1)
    
    return answer + '0' + answer[::-1]
