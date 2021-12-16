# 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = 1
    stack = []
    
    for v in s:
        stacklen = len(stack)
        while stack and stack[-1] == v: 
            stack.pop()
        if stacklen == len(stack): 
            stack.append(v)

    if stack: answer = 0
    return answer
