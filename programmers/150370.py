# 개인정보 수집 유효기간
# https://school.programmers.co.kr/learn/courses/30/lessons/150370

from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    d = {}
    for term in terms:
        k, v = term.split(' ')
        d[k] = int(v)
    
    for i, privacy in enumerate(privacies):
        date, t = privacy.split(' ')
        year, month, day = date.split('.')
        t_year, t_month, t_day = today.split('.')

        if datetime(int(t_year), int(t_month), int(t_day)) >= \
            datetime(int(year), int(month), int(day)) + relativedelta(months=d[t]):
            answer.append(i + 1)

    return answer
