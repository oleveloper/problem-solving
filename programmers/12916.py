# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    cntp = 0
    
    for c in s:
        if c == 'p' or c == 'P':
            cntp += 1
        elif c == 'y' or c == 'Y':
            cntp -= 1
    
    if cntp == 0: answer = True
    else: answer = False

    return answer
