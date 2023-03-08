# [3차] 파일명 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    answer = []
    li = []
    
    for f in files:
        m = re.match('((?i)[a-z- \.]+)([0-9]+)(.*)', f)
        li.append((["head", (m.group(1)).lower()], ["number", int(m.group(2))], ["tail", m.group(3)], ["name", f]))

    li.sort(key=lambda x:(x[0], x[1]))
    for x in li: answer.append(x[3][1])

    return answer
