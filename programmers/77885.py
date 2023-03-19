# 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    
    for number in numbers:
        strnum = list(format(number, '064b'))
        if number % 2 == 0:
            strnum[-1] = '1'
        else:
            idx = strnum[::-1].index('0')
            strnum[-idx] = '0'
            strnum[-idx-1] = '1'
        answer.append(int(''.join(strnum), 2))

    return answer
