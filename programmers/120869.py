# 외계어 사전
# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    dic = [x for x in dic if len(spell) <= len(x)]
    
    for s in spell:
        for i in range(len(dic)):
            dic[i] = dic[i].replace(s, '', 1)
    
    return 1 if dic.count('') > 0 else 2
