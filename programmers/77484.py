# 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    d = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    zero = lottos.count(0)
    match = len(list(set(lottos) & set(win_nums)))
    
    return [d[match+zero], d[match]]
