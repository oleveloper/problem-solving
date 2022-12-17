# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    
    for x in range(1, len(s) + 1):
        s.rotate(-1)
        stack = []
        
        for y in s:
            if stack:
                if stack[-1] == '(' and y == ')': stack.pop()
                elif stack[-1] == '{' and y == '}': stack.pop()
                elif stack[-1] == '[' and y == ']': stack.pop()
                else: stack.append(y)
            else: 
                stack.append(y)
        if len(stack) == 0: answer += 1
        
    return answer
