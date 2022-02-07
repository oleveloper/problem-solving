# 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    tmp = []
    
    s = sorted(s[2 : -2].replace('{', '').split('},'), key=lambda x:len(x))
    
    for x in s: 
        splited = x.split(',')
        answer.append(int(list(set(splited) - set(tmp))[-1]))
        tmp = splited
    
    return answer
