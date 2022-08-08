# [3차] 방금그곡
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

from datetime import datetime

def solution(m, musicinfos):
    d  = {"C#": 'V', "D#": 'W', "F#": 'X',"G#": 'Y', "A#": 'Z'}
    li = [0, ""]
    
    for k, v in d.items():
        m = m.replace(k, v)
    
    for infos in musicinfos:
        info = infos.split(',')
        melody = ''
        minutes = interval(info[0], info[1])
        
        for k, v in d.items():
            info[3] = info[3].replace(k, v)

        while minutes > len(melody): melody += info[3]
        melody = melody[:minutes]
        
        if melody.find(m) != -1 and li[0] < minutes:
            li[0] = minutes
            li[1] = info[2]

    if li[0] == 0: return "(None)"
    else: return li[1]

def interval(start, end):
    start = datetime.strptime(start,"%H:%M")
    end = datetime.strptime(end,"%H:%M")
    return (end - start).seconds // 60
