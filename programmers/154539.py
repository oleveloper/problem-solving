# 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

from collections import deque

def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = deque()
    
    for i, v in enumerate(numbers):
        while len(stack) and stack[-1][1] < v:
            answer[stack[-1][0]] = v
            stack.pop()
        stack.append([i, v])

    return answer
