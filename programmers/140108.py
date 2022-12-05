# 문자열 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    yx, nx = 0, 0
    cx = ''
    
    for i, c in enumerate(s):
        if cx == '':
            cx = c
            yx += 1
        elif yx != nx: 
            if cx != c:
                nx += 1
            elif cx == c:    
                yx += 1

        if yx == nx or i == len(s) - 1:
            cx = ''
            yx = nx = 0
            answer += 1
            
    return answer
