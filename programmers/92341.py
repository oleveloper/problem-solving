# 주차 요금 계산
# https://programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil

def solution(fees, records):
    answer = []
    d = {}
    
    def time(timestr):
        timelist = timestr.split(':')
        return int(timelist[0]) * 60 + int(timelist[1])
    
    for record in records:
        r = record.split(' ')
        r[0] = time(r[0])
        if r[1] in d: d[r[1]].append([r[0], r[2]])
        else: d[r[1]] = [[r[0], r[2]]]
    
    for k, v in d.items():
        m, f = 0, 0
        for r in v:
            if r[1] == 'IN': m -= r[0]
            else: m += r[0]
        
        if len(v) % 2 == 1: m += time('23:59')

        if m <= fees[0]: f = fees[1]
        else: f = fees[1] + ceil((m - fees[0]) / fees[2]) * fees[3]
        d[k] = f
    
    answer = [v for k, v in sorted(d.items())]
    return answer

