# [1차] 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677

import copy

def split_string(s):
    li = []
    l, r = 0, 2
    while r <= len(s):
        li.append([s[l:r:]])
        l += 1
        r += 1
    return li

def validate_string(l):
    return [x[0].lower() for x in l if (x[0]).isalpha()]

def calculate(li1, li2):
    li = []
    for x in li1:
        if x in li2:
            li.append(x)
            li2.remove(x)
    
    l1 = len(li)
    l2 = len(li1 + li2)
    return (1 if l2 == 0 else l1) / (1 if l2 == 0 else l2)
    
def solution(str1, str2):
    answer = 0
    li1 = validate_string(split_string(str1))
    li2 = validate_string(split_string(str2))    
    return int(calculate(copy.deepcopy(li1), copy.deepcopy(li2)) * 65536)
