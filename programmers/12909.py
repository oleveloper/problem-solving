# 올바른 괄호
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    
    for p in s:
        if len(stack) > 0 and stack[-1] and p == ')': stack.pop(-1)
        else: stack.append(p)
            
    if len(stack) == 0: return True
    return False
