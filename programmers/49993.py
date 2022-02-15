# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        d = {_ : 999 for _ in skill}
        for i, v in enumerate(skill):
            if v != skill[0] and d[skill[i - 1]] == -1: break
            if v in tree: d[v] = tree.index(v)
        
        s = ''.join([x for x, y in sorted(d.items(), key = lambda x : x[1])])
        if s == skill: answer += 1
    
    return answer
