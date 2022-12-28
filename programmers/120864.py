# 숨어있는 숫자의 덧셈 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120864

def solution(my_string):
    answer = 0
    num = ''
    
    for x in my_string:
        if x.isdigit(): num += x
        elif num != '':
            answer += int(num)
            num = ''
    
    if num != '': answer += int(num)
    return answer
