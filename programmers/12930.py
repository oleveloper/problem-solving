# 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''
    words = s.split(' ')
    
    for word in words:
        for i, v in enumerate(word):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
    
    return answer[:-1]
