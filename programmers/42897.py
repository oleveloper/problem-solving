# 도둑질
# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0
    dp1, dp2 = [0] * len(money), [0] * len(money)
    
    dp1[0] = money[0]
    dp1[1] = max(dp1[0], money[1])
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])
    
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    answer = max(max(dp1), max(dp2))
    return answer
