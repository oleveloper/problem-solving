# 햄버거 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    l = []
    
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1, 2, 3, 1]:
            answer += 1
            for i in range(4): l.pop()
    
    return answer
