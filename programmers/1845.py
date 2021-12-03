# 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = list(set(nums))
    tmp = []

    for v in nums:
        if v not in tmp: 
            tmp.append(v)
            answer += 1
            if answer == n: 
                break
    
    return answer
