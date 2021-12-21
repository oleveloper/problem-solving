# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        p = prices[i]
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if p > prices[j]: break
        answer.append(cnt)
    
    return answer
