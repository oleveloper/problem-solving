# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    answer = arr
    
    answer.remove(sorted(arr)[0])
    if len(answer) == 0:
        answer.append(-1)
    
    return answer
