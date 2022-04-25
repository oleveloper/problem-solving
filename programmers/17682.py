# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re

def solution(dartResult):
    answer = 0
    bonus = {'S':1, 'D':2, 'T':3}
    option = {'*': 2, '#': -1}
    star = False
    pattern = '[0-9]+[A-Z][\*#]?'
    li = re.findall(pattern, dartResult)
    
    for x in li[::-1]:
        n = int(re.findall('[0-9]+', x)[0])
        s = re.findall('[A-Z]', x)[0]
        o = re.findall('[\*#]', x)
        tmp = n ** bonus.get(s)
        
        if star:
            tmp *= 2
            star = False
        if len(o) > 0:
            if o[0] == '*': star = True
            tmp *= option.get(o[0])
        
        answer += tmp
    
    return answer
