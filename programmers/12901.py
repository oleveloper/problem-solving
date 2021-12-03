# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    d = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    mon = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    for i in range(1, a):
        b += mon[i]
    
    answer = d[b % 7]
    return answer
