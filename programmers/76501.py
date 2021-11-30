# 음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    
    for i, v in enumerate(absolutes):
        if signs[i]:
            answer += v
        else:
            answer -= v
    
    return answer
