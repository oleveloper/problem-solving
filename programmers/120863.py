# 다항식 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    answer = ''
    x, i = 0, 0
    
    p = polynomial.split('+')
    for c in p:
        if 'x' in c:
            x += 1 if c.strip()[:-1] == '' else int(c.strip()[:-1])
        else:
            i += int(c)
    
    if x == 1:
        answer += 'x'
    elif x != 0:
        answer += '{0}x'.format(x)

    if i != 0 and x != 0:
        answer += ' + {0}'.format(i)
    elif i != 0:
        answer += str(i)

    return answer
