# 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    d = {}
    
    for v in record:
        if v.startswith("Enter") or v.startswith("Change"):
            d[v[v.find(' ') + 1:v.rfind(' ')]] = v[v.rfind(' ') + 1:]
        
    for v in record:
        vl = v.split(' ')
        if vl[0] == "Enter":
            answer.append(d.get(vl[1]) + "님이 들어왔습니다.")
        if vl[0] == "Leave":
            answer.append(d.get(vl[1]) + "님이 나갔습니다.")

    return answer
