# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(idx, res):
        if idx == n:
            if res == target: 
                nonlocal answer 
                answer += 1
            return
        else:
            dfs(idx + 1, res + numbers[idx])
            dfs(idx + 1, res - numbers[idx])
    
    dfs(0, 0)
    return answer
