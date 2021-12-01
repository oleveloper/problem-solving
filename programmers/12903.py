# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    i = len(s) // 2
    
    if len(s) % 2 == 0:
        answer += s[i-1] + s[i]
    else:
        answer = s[i]
    
    return answer
