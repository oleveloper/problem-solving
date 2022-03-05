# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    answer = len([i for i, v in enumerate(citations) if i < v])
    
    return answer
