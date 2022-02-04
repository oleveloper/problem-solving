# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    d, l = {}, {}

    for i in range(len(genres)):
        if genres[i] in d: d[genres[i]] += plays[i]
        else: d[genres[i]] = plays[i]

        if genres[i] in l: l[genres[i]].append(plays[i])
        else: l[genres[i]] = [plays[i]]
    
    d = sorted(d.items(), reverse=True, key=lambda x:x[1])
    l = {x:sorted(l[x], reverse=True)[:2] for x in l.keys()}

    for left, right in d:
        for v in l.pop(left):
            answer.append(plays.index(v))
            plays[answer[-1]] = 0
            
    return answer
