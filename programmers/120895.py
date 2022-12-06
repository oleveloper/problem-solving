# 인덱스 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/120895

def solution(my_string, num1, num2):
    l = list(my_string)
    l[num2], l[num1] = l[num1], l[num2]
    
    return ''.join(l)
