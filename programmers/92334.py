# 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    dcnt = dict.fromkeys(id_list, 0)
    dname = dict.fromkeys(id_list, None)
    report = set(report)
    
    for v in report:
        reporter = v.split(' ')[0]
        reported = v.split(' ')[1]
        dcnt[reported] += 1
        if dname[reporter] is None: dname[reporter] = [reported]
        else: dname[reporter].append(reported)

    dcnt = { key : value for key, value in dcnt.items() if value >= k }
    
    for k, v in dname.items():
        cnt = 0
        if v is not None:
            for vv in v:
                if vv in dcnt: cnt += 1
        answer.append(cnt)
    
    return answer
