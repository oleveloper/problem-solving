# [PCCE 기출문제] 9번 / 지폐 접기
# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    wx, wy = wallet
    bx, by = bill
    
    while min(bx, by) > min(wx, wy) or max(bx, by) > max(wx, wy):
        if bx > by:
            bx = bx // 2
        else:
            by = by // 2
        answer += 1

    return answer
