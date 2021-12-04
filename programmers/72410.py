# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*\(\)=+\[\{\]\}:\?,<>/]', '', new_id)
    new_id = re.sub('\.{2,}', '.', new_id)
    while new_id.startswith('.'): new_id = new_id[1:]
    while new_id.endswith('.'): new_id = new_id[:-1]
    if len(new_id) == 0: new_id = 'a'
    elif len(new_id) >= 16: new_id = new_id[:15]
    while new_id.endswith('.'): new_id = new_id[:-1]
    while len(new_id) <= 2: new_id += new_id[-1]        
    
    answer = new_id
    return answer
