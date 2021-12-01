# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = [arr[0]]
    
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
        
    return answer
