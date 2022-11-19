# 분수의 덧셈
# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(denum1, num1, denum2, num2):
    num = num1 * num2
    denum = denum1 * num2 + denum2 * num1
    
    x, y = num, denum
    while x: y, x = x, y % x
    
    return [denum // y, num // y]
